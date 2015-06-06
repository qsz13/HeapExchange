
from django.db import models


class Announcement(models.Model):

    title = models.CharField(max_length=20)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title