from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField
from django.db.models.signals import post_save
from HeapExchange.settings import REFER_COIN, REGISTER_COIN
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
    avatar = AvatarField(upload_to='avatar',default="default.png",width=100, height=100)
    referral = models.ForeignKey('auth.User', null=True, related_name='refered_user')


    def __unicode__(self):
        return self.user.username

    def refer(self, new_user):
        self.user.balance.amount += REFER_COIN
        self.user.balance.save()
        # TODO:
        # create a transaction record
        new_user.referral = self
        new_user.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def create_user_balance(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance, amount=REGISTER_COIN)

post_save.connect(create_user_profile, sender=User)
post_save.connect(create_user_balance, sender=User)