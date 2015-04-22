from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500, null=True)
    deadline = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100, null=True)
    requirement = models.CharField(max_length=500, null=True)
    initialtime = models.DateTimeField(auto_now=True)
    limit = models.IntegerField(null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Course(Post):
    initiator = models.ForeignKey(User, default=1, related_name='initiator')
    joined = models.ManyToManyField(User, related_name="joins")
    interested = models.ManyToManyField(User, related_name="interests")
    price = models.IntegerField(default=0)


class Activity(Post):
    pass


class Tag(models.Model):
    pass
