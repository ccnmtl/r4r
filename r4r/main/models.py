# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class LinkedModel(models.Model):
    next = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)


class Prompt(LinkedModel):
    details = models.TextField(default='')
    media_url = models.TextField(null=True)
    release_date = models.DateTimeField(auto_now_add=True)


class Case(LinkedModel):
    head = models.ForeignKey(Prompt, null=True, on_delete=models.SET_NULL)
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
        User, related_name='instructor_set', blank=True)
    title = models.CharField(max_length=256, blank=True, default='')


class Rotation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    head = models.ForeignKey(Case, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256)


class Team(models.Model):
    rotation = models.ForeignKey(Rotation, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    number = models.IntegerField()


class Discussion(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, null=True, on_delete=models.CASCADE)


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
