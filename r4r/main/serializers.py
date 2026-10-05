from django.contrib.auth.models import User
from r4r.main.models import Course, Team, Day, Rotation, Case
from rest_framework import serializers
# from r4r.settings import TEAM_COUNT
# from random import shuffle


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    rotations = serializers.SerializerMethodField('get_rotations')

    def get_rotations(self, instance):
        rotations = self.instance.rotation_set.all()
        return [
            {'title': rotation.title,
                'cases': [{'title': case.title,
                           'days': case.get_days()}
                          for case in rotation.get_cases()]}
            for rotation in rotations]

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        course = super().create(validated_data)

        for title in ['Emergency Medicine', 'OB/GYN', 'Pediatrics']:
            Rotation.objects.create(title=title, course=course)

        """ EVAN'S NOTES - SEPTEMBER 29, 2026
        SOMEHOW I NEED TO PULL NEW AND CURRENT STUDENTS INTO THE COURSE.
        I THEN NEED TO:
            - PULL THE COURSE DATA FROM COURSEWORKS
            - GET THE TITLE, CODE,
            - PULL THE ROSTER DATA RELATED TO THE COURSE FROM COURSEWORKS
            - ADD THE ROSTER TO THE COURSE ROSTER
            - SPLIT THE ROSTER INTO ROUGHLY EQUAL TEAMS
        THE PROCESS MIGHT HAVE TO EXIST IN ANOTHER METHOD OR CLASS BUT IT WOULD
        LOOK SOMETHING LIKE THIS:

        roster = self.instance.roster.all()
        team_num = TEAM_COUNT

        shuffle(roster)

        while team_num > 0:
            remainder = len(roster)
            members = [roster.pop() for x in range(int(remainder / team_num))]
            Team.objects.create(course=course, members=members,
                                leader=members[0])
            team_num -= 1
        """

        return course


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class RotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rotation
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
