from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save


class Profile(models.Model):


    GENDER_CHOICE = (
        ("M", "Male"),
        ("F", "Female"),
    )

    user = models.OneToOneField('auth.User')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13)


    def __unicode__(self):
        return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)