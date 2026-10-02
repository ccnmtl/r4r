# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Form(models.Model):
    questions = ArrayField(models.TextField(default=''))


class Page(models.Model):
    def get_next(self):
        self.next = self.next.next
        self.save()

    form = models.ForeignKey(Form, null=True, on_delete=models.SET_NULL)
    next = models.ForeignKey('self', null=True, on_delete=get_next)


class Course(models.Model):
    def get_head(self):
        self.head = self.head.next
        self.save()

    def get_instructors(self):
        return self.object.roster.filter(is_staff=True)

    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    roster = models.ManyToManyField(User)
    title = models.CharField(max_length=256)
    code = models.TextField(default='', unique=True)  # Ex: 2026-F-[course#]
    head = models.ForeignKey(Page, on_delete=get_head, null=True)


class Team(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)


class Post(models.Model):
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)


class Forum(models.Model):
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    question = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
