from django.contrib.auth.models import User
from django.db import models





# TODO change model

class Post(models.Model):
    created_time = models.DateTimeField()
    creator = models.OneToOneField(User)
    title = models.CharField(max_length=32)
    description = models.TextField()
    flag_times = models.IntegerField(null=True)
    flag_user = models.ManyToManyField(User, related_name="flag_post")



class Course(models.Model):
    skill_requirement = models.CharField(max_length=30)
    link = models.URLField()
    student_limit = models.IntegerField()
    price = models.IntegerField()
    tag = models.ManyToManyField("Tag")
    place = models.CharField(max_length=20)

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name