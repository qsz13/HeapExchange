from django.contrib.auth.models import User
from django.db import models


class Balance(models.Model):
    user = models.OneToOneField(User)
    amount = models.IntegerField()

    def __unicode__(self):
        return self.user.username+"'s balance"



class Transfer(models.Model):
    from_user = models.OneToOneField(User, related_name="expense")
    to_user = models.OneToOneField(User, related_name="income")
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)