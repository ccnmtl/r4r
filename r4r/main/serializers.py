from django.contrib.auth.models import User
from r4r.main.models import (
    Course, Team, Rotation, Case, Prompt
)
from rest_framework import serializers
from r4r.main.utils import fetch_courseworks_data, get_ll
from re import match, search


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class PromptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prompt
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamRefSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.SerializerMethodField('get_members')

    def get_members(self, instance):
        return [
            f'{user['url']}: {user['username']}'
            for user in UserSerializer(
                instance.members,
                many=True,
                context=self.context).data]

    class Meta:
        model = Team
        fields = ['url', 'number', 'members']


class CourseListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = [
            'url', 'id', 'title', 'code', 'courseworks', 'created_at',
            'details', 'is_active'
        ]


class RotationSerializer(serializers.HyperlinkedModelSerializer):
    case = serializers.SerializerMethodField('get_case')
    team = serializers.SerializerMethodField('get_team')

    class Meta:
        model = Rotation
        fields = ['url', 'title', 'head', 'course', 'case', 'team']

    def get_case(self, instance):
        return CaseSerializer(
            get_ll(instance.head), many=True, context=self.context).data

    def get_team(self, instance):
        return TeamRefSerializer(
            Team.objects.filter(rotation=instance),
            many=True,
            context=self.context).data


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    rotations = serializers.SerializerMethodField('get_rotations')

    def get_rotations(self, instance):
        return RotationSerializer(
            instance.rotation_set.all(),
            many=True,
            context=self.context).data

    class Meta:
        model = Course
        fields = [
            'url', 'title', 'code', 'courseworks', 'is_active', 'created_at',
            'details', 'instructors', 'rotations'
        ]

    def validate_courseworks(self, value):
        """
        Check that the course exists in CourseWorks
        """
        data = fetch_courseworks_data(
            f'courses/{value}')
        if data is None:
            raise serializers.ValidationError("Course ID not found")
        data_2 = fetch_courseworks_data(
            f'courses/{value}/enrollments')
        if data_2 is None:
            raise serializers.ValidationError("Course Enrollments not found")
        return value

    def generate_team(self, group_id, number, rotation):
        members = []
        team_data = fetch_courseworks_data(f'groups/{group_id}/users')
        member_data = map(lambda user: user['login_id'], team_data)
        for member in member_data:
            members.append(User.objects.get(username=member))
        team = Team.objects.create(
            rotation=rotation, number=number)
        team.members.set(members)
        team.save()

    def create(self, validated_data):
        course = super().create(validated_data)

        courseworks = course.courseworks
        course_data = fetch_courseworks_data(
            f'courses/{courseworks}')
        if course.title == '':
            course.title = course_data['name']
        if course.code == '':
            course.code = course_data['course_code']
        course.save()

        enrollments = fetch_courseworks_data(
            f'courses/{courseworks}/enrollments')

        roster = []

        for enrollment in enrollments:
            if enrollment['enrollment_state'] == "active":
                user_data = enrollment['user']
                (last, first) = user_data['sortable_name'].split(', ')
                is_staff = 'student' not in enrollment['role'].lower()
                (user, _) = User.objects.get_or_create(
                    username=user_data['login_id'],
                    defaults={
                        'first_name': first,
                        'last_name': last,
                        'email': f'{user_data['login_id']}@columbia.edu',
                        'is_staff': is_staff})
                if is_staff:
                    course.instructors.add(user)
                else:
                    roster.append(user)

        group_data = fetch_courseworks_data(
            f'courses/{courseworks}/groups')
        filtered_groups = filter(
            lambda group: match(r'^team *\d+', group['name'].lower().strip()),
            group_data)
        teams = map(lambda group: (
            group['id'],
            search(r'\d+$', group['name']).group()),
            filtered_groups)

        for title in ['Medicine']:
            rotation = Rotation.objects.create(title=title, course=course)

            for (group_id, number) in teams:
                self.generate_team(group_id, number, rotation)
        return course


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff']
