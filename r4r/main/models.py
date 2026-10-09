# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class LinkedModel(models.Model):
    head = None
    next = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)


class Form(models.Model):
    prompt = models.TextField(null=True)
    media_url = models.TextField(null=True)


class Task(LinkedModel):
    details = models.TextField(default='')
    form = models.ForeignKey(Form, null=True, on_delete=models.SET_NULL)
    release_date = models.DateTimeField(auto_now_add=True)


class Day(LinkedModel):
    details = models.TextField(default='')
    head = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256, null=True)


class Case(LinkedModel):
    head = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256, null=True)


class Course(models.Model):
    def get_instructors(self):
        return self.object.roster.filter(is_staff=True)

    code = models.CharField(max_length=256, default='', unique=True)
    courseworks = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField(default='')
    is_active = models.BooleanField(default=False)
    instructors = models.ManyToManyField(
        User, related_name='instructors', blank=True)
    roster = models.ManyToManyField(User, blank=True)
    title = models.CharField(max_length=256, blank=True, default='')


class Rotation(LinkedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    head = models.ForeignKey(Case, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256)


class Team(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)


class Forum(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    question = models.TextField()
    day = models.ForeignKey(Day, null=True, on_delete=models.CASCADE)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, null=True, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
