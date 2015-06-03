from django.contrib.auth.models import User
from django.db import models


class Balance(models.Model):
    user = models.OneToOneField(User)
    amount = models.IntegerField()

    def __unicode__(self):
        return self.user.username+"'s balance"



class Transfer(models.Model):
    from_user = models.OneToOneField(User, related_name="expense", null=True)
    to_user = models.OneToOneField(User, related_name="income")
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True,null=True)
    def __unicode__(self):
        return "transfer from "+str(self.from_user)+" to "+str(self.to_user)


def transfer(from_user, to_user, amount):
    if from_user.balance < amount:
        return False
    else:
        from_user.balance.amount = from_user.balance.amount - amount
        to_user.balance.amount = to_user.balance.amount + amount
        from_user.balance.save()
        to_user.balance.save()
        Transfer.objects.create(from_user=from_user, to_user=to_user, amount=amount)
        return True