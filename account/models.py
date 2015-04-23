from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.db.models.signals import post_save
from awesome_avatar.fields import AvatarField
from coin.models import Balance


class Profile(models.Model):


    GENDER_CHOICE = (
        ("M", "Male"),
        ("F", "Female"),
    )

    user = models.OneToOneField('auth.User')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True, blank=False, default=None)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    school = models.CharField(max_length=15, null=True, blank=True)
    timetable = models.CharField(max_length=77, default="0"*77)
    interest_tag = models.ManyToManyField('post.Tag', related_name="interest_profile", blank=True)
    avatar = AvatarField(upload_to='avatar', width=100, height=100)



    def __unicode__(self):
        return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def create_user_balance(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance, amount=50)

post_save.connect(create_user_profile, sender=User)
post_save.connect(create_user_balance, sender=User)