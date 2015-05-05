from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    time = models.DateField(null=True)
    description = models.CharField(max_length=500, null=True)
    deadline = models.DateField(null=True)
    location = models.CharField(max_length=100, null=True)
    requirement = models.CharField(max_length=500, null=True)
    initialtime = models.DateTimeField(auto_now=True)
    limit = models.IntegerField(null=True)

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
        path = reverse('detail', args=[self.flag, self.id])
        return path


class Activity(Post):
    initiator = models.ForeignKey(User, default=1, related_name='activities')
    joined = models.ManyToManyField(User, related_name="joined_activities",  blank=True)
    interested = models.ManyToManyField(User, related_name="interested_activities",  blank=True)
    flag = models.CharField(max_length=1, default='a')

    def get_absolute_url(self):
        path = reverse('detail', args=[self.flag, self.id])
        return path

class Tag(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course, related_name='tags')
    activity = models.ManyToManyField(Activity, related_name='tags')

    def __unicode__(self):
        return self.name
