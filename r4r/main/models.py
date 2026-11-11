# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    title = models.CharField(max_length=256, null=True)
    details = models.TextField(default='')
    media_url = models.TextField(null=True)
    next = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.id})'


class Case(models.Model):
    head = models.ForeignKey(Prompt, null=True, on_delete=models.SET_NULL)
    next = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f'{self.title} ({self.id})'


class Course(models.Model):
    def get_instructors(self):
        return self.object.roster.filter(is_staff=True)

    code = models.CharField(max_length=256, default='', unique=True)
    courseworks = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField(default='')
    is_active = models.BooleanField(default=False)
    instructors = models.ManyToManyField(
        User, related_name='instructor_set', blank=True)
    title = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return f'{self.title} ({self.id})'


class Rotation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    head = models.ForeignKey(Case, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.title} - {self.course}'


class Team(models.Model):
    rotation = models.ForeignKey(Rotation, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    number = models.IntegerField()

    def __str__(self):
        return f'Team {self.number}, {self.rotation}'


class Discussion(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prompt} {self.team} Discussion {self.id}'


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(
        Discussion, null=True, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    unread = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
