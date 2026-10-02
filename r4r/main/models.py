# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class LinkedModel(models.Model):
    def get_chain(self):
        target = self.head
        chain = []
        while target:
            chain.append(target)
            target = target.next
        return chain

    def set_next(self):
        if self.next:
            self.next = self.next.next
            self.save()

    def set_head(self):
        if self.head:
            self.head = self.head.next
            self.save()

    head = None
    next = models.ForeignKey('self', null=True, on_delete=set_next)


class Form(models.Model):
    prompt = models.TextField(null=True)
    media_url = models.TextField(null=True)


class Task(LinkedModel):
    def set_next(self):
        return super().set_next()

    details = models.TextField(default='')
    form = models.ForeignKey(Form, null=True, on_delete=models.SET_NULL)
    release_date = models.DateTimeField(auto_now_add=True)


class Day(LinkedModel):
    def set_head(self):
        return super().set_head()

    def get_tasks(self) -> list[Task]:
        return super().get_chain()

    details = models.TextField(default='')
    head = models.ForeignKey(Task, null=True, on_delete=set_head)
    title = models.CharField(max_length=256, null=True)
    week = models.IntegerField()


class Case(LinkedModel):
    def set_head(self):
        return super().set_head()

    def get_days(self) -> list[Task]:
        return super().get_chain()

    head = models.ForeignKey(Task, null=True, on_delete=set_head)
    title = models.CharField(max_length=256, null=True)


class Course(models.Model):
    def get_instructors(self):
        return self.object.roster.filter(is_staff=True)

    code = models.CharField(max_length=256, default='', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField(default='')
    is_active = models.BooleanField(default=False)
    instructors = models.ManyToManyField(User, related_name='instructors')
    roster = models.ManyToManyField(User)
    title = models.CharField(max_length=256)


class Rotation(LinkedModel):
    def set_head(self):
        return super().set_head()

    def get_cases(self) -> list[Case]:
        return super().get_chain()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    head = models.ForeignKey(Case, null=True, on_delete=set_head)
    title = models.CharField(max_length=256)


class Team(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    leader = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='leader')


class Forum(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    question = models.TextField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    is_edited = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    text = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
