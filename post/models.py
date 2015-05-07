#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models



class OneTimeSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class SequenceTimeSchedule(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class WeeklyTimeSchedule(models.Model):

    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Post(models.Model):

    ONE_TIME = "ONCE"
    SEQUENCE_TIME = "SEQU"
    WEEKLY_TIME = "WEEK"
    CUSTOMIZE_TIME = "CUST"

    SCHEDULE_TYPE = (
        (ONE_TIME, u"当天结束"),
        (SEQUENCE_TIME, u"连续多天"),
        (WEEKLY_TIME, u"每周举行"),
        (CUSTOMIZE_TIME, u"自定义"),
    )


    title = models.CharField(max_length=100, null=True)
    time = models.DateField(null=True)
    description = models.CharField(max_length=500, null=True)
    deadline = models.DateField(null=True)
    location = models.CharField(max_length=100, null=True)
    requirement = models.CharField(max_length=500, null=True)
    initialtime = models.DateTimeField(auto_now=True)
    limit = models.IntegerField(null=True)
    schedule_type = models.CharField(max_length=4, null=True)
    one_time_schedule = models.ForeignKey(OneTimeSchedule, null=True)
    sequence_time_schedule = models.ForeignKey(SequenceTimeSchedule, null=True)
    weekly_time_schedule = models.ForeignKey(WeeklyTimeSchedule, null=True)


    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Course(Post):
    initiator = models.ForeignKey(User, default=1, related_name='courses')
    joined = models.ManyToManyField(User, related_name="joined_courses",  blank=True)
    interested = models.ManyToManyField(User, related_name="interested_courses",  blank=True)
    price = models.IntegerField(default=0)
    flag = models.CharField(max_length=1, default='c')

    def get_absolute_url(self):
        path = reverse('post:detail', args=[self.flag, self.id])
        return path


class Activity(Post):
    initiator = models.ForeignKey(User, default=1, related_name='activities')
    joined = models.ManyToManyField(User, related_name="joined_activities",  blank=True)
    interested = models.ManyToManyField(User, related_name="interested_activities",  blank=True)
    flag = models.CharField(max_length=1, default='a')

    def get_absolute_url(self):
        path = reverse('post:detail', args=[self.flag, self.id])
        return path

class Tag(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course, related_name='tags')
    activity = models.ManyToManyField(Activity, related_name='tags')

    def __unicode__(self):
        return self.name


