from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, default='DEFAULT')
    time = models.DateTimeField(default=datetime.now())
    description = models.CharField(max_length=500, default='DEFAULT')
    deadline = models.DateTimeField(default=datetime.now())
    location = models.CharField(max_length=100, default='DEFAULT')
    requirement = models.CharField(max_length=500, default='DEFAULT')
    initialtime = models.DateTimeField(default=datetime.now())
    limit = models.IntegerField(default=10)

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
