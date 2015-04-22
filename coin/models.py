from django.contrib.auth.models import User
from django.db import models


class Balance(models.Model):
    user = models.OneToOneField(User)
    amount = models.IntegerField()



class Transfer(models.Model):
    from_user = models.OneToOneField(User, related_name="expense")
    to_user = models.OneToOneField(User, related_name="income")
    amount = models.IntegerField()