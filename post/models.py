#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models


class OneTimeSchedule(models.Model):
    once_date = models.DateField(verbose_name=u'活动日期')
    once_start_time = models.TimeField(verbose_name=u'开始时间')
    once_end_time = models.TimeField(verbose_name=u'结束时间')


class SequenceTimeSchedule(models.Model):
    sequence_start_date = models.DateField()
    sequence_end_date = models.DateField()
    sequence_start_time = models.TimeField()
    sequence_end_time = models.TimeField()


class WeeklyTimeSchedule(models.Model):
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    weekly_start_date = models.DateField()
    weekly_end_date = models.DateField()
    weekly_start_time = models.TimeField()
    weekly_end_time = models.TimeField()


class Post(models.Model):
    ONE_TIME = "ONCE"
    SEQUENCE_TIME = "SEQU"
    WEEKLY_TIME = "WEEK"
    #CUSTOMIZE_TIME = "CUST"

    SCHEDULE_TYPE = (
        (ONE_TIME, u"当天结束"),
        (SEQUENCE_TIME, u"连续多天"),
        (WEEKLY_TIME, u"每周举行"),
        #(CUSTOMIZE_TIME, u"自定义"),
    )

    title = models.CharField(max_length=100, null=True, verbose_name=u'标题')
    description = models.CharField(
        max_length=500, null=True, verbose_name=u'描述')
    deadline = models.DateField(null=True, verbose_name=u'报名截至')
    location = models.CharField(max_length=100, null=True, verbose_name=u'地点')
    requirement = models.CharField(
        max_length=500, null=True, verbose_name=u'需求')
    initialtime = models.DateTimeField(auto_now=True, )
    limit = models.IntegerField(null=True, verbose_name=u'人数限制')
    schedule_type = models.CharField(max_length=4, null=True)
    one_time_schedule = models.OneToOneField(
        OneTimeSchedule, null=True, blank=True)
    sequence_time_schedule = models.OneToOneField(
        SequenceTimeSchedule, null=True, blank=True)
    weekly_time_schedule = models.OneToOneField(
        WeeklyTimeSchedule, null=True, blank=True)

    def get_post_schedule(self):

        if self.schedule_type == 'ONCE':

            schedule = self.one_time_schedule

            return str(schedule.once_date) + ' ' + '{:%H:%M}'.format(
                schedule.once_start_time) + u'至' + '{:%H:%M}'.format(schedule.once_end_time)

        elif self.schedule_type == 'SEQU':

            schedule = self.sequence_time_schedule

            return str(schedule.sequence_start_date) + u' 至 ' + str(
                schedule.sequence_end_date) + u' 每天 ' + '{:%H:%M}'.format(
                schedule.sequence_start_time) + u'至' + '{:%H:%M}'.format(schedule.sequence_end_time)
        elif self.schedule_type == 'WEEK':
            schedule = self.weekly_time_schedule

            s = str(schedule.weekly_start_date) + u' 至 ' + \
                str(schedule.weekly_end_date) + u' 每周 '
            if schedule.monday:
                s += u'一 '
            if schedule.tuesday:
                s += u'二 '
            if schedule.wednesday:
                s += u'三 '
            if schedule.thursday:
                s += u'四 '
            if schedule.friday:
                s += u'五 '
            if schedule.saturday:
                s += u'六 '
            if schedule.sunday:
                s += u'日 '
            s = s + '{:%H:%M}'.format(
                schedule.weekly_start_time) + u'至' + '{:%H:%M}'.format(schedule.weekly_end_time)
            return s

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Course(Post):
    initiator = models.ForeignKey(User, default=1, related_name='courses')
    joined = models.ManyToManyField(
        User, related_name="joined_courses", blank=True)
    interested = models.ManyToManyField(
        User, related_name="interested_courses", blank=True)
    price = models.IntegerField(default=0, verbose_name=u'价格')
    flag = models.CharField(max_length=1, default='c')
    has_arr = models.BooleanField(default=False)


    def get_absolute_url(self):
        path = reverse('post:detail', args=[self.flag, self.id])
        return path


class Activity(Post):
    initiator = models.ForeignKey(User, default=1, related_name='activities')
    joined = models.ManyToManyField(
        User, related_name="joined_activities", blank=True)
    interested = models.ManyToManyField(
        User, related_name="interested_activities", blank=True)
    flag = models.CharField(max_length=1, default='a')

    def get_absolute_url(self):
        path = reverse('post:detail', args=[self.flag, self.id])
        return path


class Arrangement(models.Model):
    course = models.ForeignKey(Course, default=1, related_name='arrangements')
    order = models.IntegerField(null=True)
    content = models.CharField(max_length=100, null=True, blank=True)
    time = models.DateField(null=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course, related_name='tags')
    activity = models.ManyToManyField(Activity, related_name='tags')

    def __unicode__(self):
        return self.name


class CourseImages(models.Model):
    post = models.ForeignKey(Course, related_name="images", null=True)
    image_file = models.ImageField(upload_to="imgs", null=True)

class ActivityImages(models.Model):
    post = models.ForeignKey(Activity, related_name="images", null=True)
    image_file = models.ImageField(upload_to="imgs", null=True)