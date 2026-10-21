from django.contrib.auth.models import User
from r4r.main.models import Course, Team, Rotation, Case
from rest_framework import serializers
from r4r.main.utils import fetch_courseworks_data, get_ll
from r4r.settings import MAX_TEAMS
from random import shuffle


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class CourseListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = [
            'url', 'id', 'title', 'code', 'courseworks', 'created_at',
            'details', 'is_active'
        ]


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    rotations = serializers.SerializerMethodField('get_rotations')

    def get_rotations(self, instance):
        def read_roster(roster):
            return [
                (f'{user['url']}: {user['username']}')
                for user in UserSerializer(
                    roster,
                    many=True,
                    context=self.context).data
            ]

        rotations = instance.rotation_set.all()

        return [{
            'title': rotation.title,
            'cases': [{
                'title': case.title,
                'days': get_ll(case.head)
                } for case in get_ll(rotation.head)],
            'roster': read_roster(rotation.roster.all())
            } for rotation in rotations]

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
        if len(roster) < 1:
            if len(roster) < MAX_TEAMS * 4:
                team_num = int(len(roster) / 4) + 1
            else:
                team_num = MAX_TEAMS

            shuffle(roster)

            while team_num > 0:
                remainder = len(roster)
                members = [roster.pop() for x in
                           range(int(remainder / team_num))]
                team = Team.objects.create(course=course)
                team.members.set(members)
                team.save()
                team_num -= 1
        for title in ['Emergency Medicine', 'OB/GYN', 'Pediatrics']:
            rotation = Rotation.objects.create(title=title, course=course)
            rotation.roster.add(roster)
            rotation.save()

        return course


class RotationSerializer(serializers.HyperlinkedModelSerializer):
    roster = serializers.SerializerMethodField('get_roster')

    class Meta:
        model = Rotation
        fields = ['url', 'title', 'course', 'head', 'roster']

    def get_roster(self, instance):
        return [
            (f'{user['url']}: {user['username']}')
            for user in UserSerializer(
                instance.roster,
                many=True,
                context=self.context).data
        ]


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff']
