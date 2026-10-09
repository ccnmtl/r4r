from django.contrib.auth.models import User
from r4r.main.models import Course, Team, Day, Rotation, Case
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
        fields = '__all__'


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    rotations = serializers.SerializerMethodField('get_rotations')

    def get_rotations(self, instance):
        rotations = instance.rotation_set.all()
        return [
            {'title': rotation.title,
                'cases': [{'title': case.title,
                           'days': get_ll(case.head)}
                          for case in get_ll(rotation.head)]}
            for rotation in rotations]

    class Meta:
        model = Course
        fields = '__all__'

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

        for title in ['Emergency Medicine', 'OB/GYN', 'Pediatrics']:
            Rotation.objects.create(title=title, course=course)
        courseworks = course.courseworks
        course_data = fetch_courseworks_data(
            f'courses/{courseworks}')
        if course.title == '':
            course.title = course_data['name']
        if course.code == '':
            course.code = course_data['course_code']

        roster = fetch_courseworks_data(
            f'courses/{courseworks}/enrollments')

        for enrollment in roster:
            if enrollment['enrollment_state'] == "active":
                user_data = enrollment['user']
                (last, first) = user_data['sortable_name'].split(', ')
                email = f'{user_data['login_id']}@columbia.edu'
                is_staff = 'student' not in enrollment['role'].lower()
                (user, _) = User.objects.get_or_create(
                    username=user_data['login_id'], first_name=first,
                    last_name=last, email=email, is_staff=is_staff)
                if is_staff:
                    course.instructors.add(user)
                else:
                    course.roster.add(user)

        students = list(course.roster.all())

        if len(students) < 48:
            team_num = len(roster) / 4
        else:
            team_num = MAX_TEAMS

        shuffle(students)

        while team_num > 0:
            remainder = len(students)
            members = [students.pop() for x in
                       range(int(remainder / team_num))]
            team = Team.objects.create(course=course)
            team.members.set(members)
            team.save()
            team_num -= 1

        return course


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class RotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rotation
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff']
