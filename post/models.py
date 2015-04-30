from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    time = models.DateField()
    description = models.CharField(max_length=500, null=True)
    deadline = models.DateField()
    location = models.CharField(max_length=100, null=True)
    requirement = models.CharField(max_length=500, null=True)
    initialtime = models.DateTimeField(auto_now=True)
    limit = models.IntegerField(null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Course(Post):
    initiator = models.ForeignKey(User, default=1, related_name='c_initiator')
    joined = models.ManyToManyField(User, related_name="c_joins")
    interested = models.ManyToManyField(User, related_name="c_interests")
    price = models.IntegerField(default=0)


    def get_absolute_url(self):
        path = reverse('course_detail', args=[self.id])
        return path


class Activity(Post):
    initiator = models.ForeignKey(User, default=1, related_name='a_initiator')
    joined = models.ManyToManyField(User, related_name="a_joins")
    interested = models.ManyToManyField(User, related_name="a_interests")


class Tag(models.Model):
    name = models.CharField(max_length=20)
    course = models.ManyToManyField(Course, related_name='tag')
    activity = models.ManyToManyField(Activity, related_name='tag')

    def __unicode__(self):
        return self.name
