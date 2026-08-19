# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


"""
Course-specific models. These change between courses. They are unaffected by
the module structure.
"""


class Course(models.Model):
    title = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='')
    instructor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)


class Post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)


"""
Module-specific models. These stay the same between courses but define the
module structure.
"""


class Form(models.Model):
    questions = ArrayField(models.TextField(default=''))


class Page(models.Model):
    def get_next(self):
        self.next = self.next.next
        self.save()

    form = models.ForeignKey(Form, null=True, on_delete=models.SET_NULL)
    next = models.ForeignKey("self", null=True, on_delete=get_next)


class Module(models.Model):
    def get_head(self):
        self.head = self.head.next
        self.save()

    head = models.ForeignKey(Page, on_delete=get_head, null=True)


class Forum(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    question = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
