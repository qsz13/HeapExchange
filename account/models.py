from django.db import models

# Create your models here.
class Profile(models.Model):


    GENDER_CHOICE = (
        ("M", "Male"),
        ("F", "Female"),
    )

    user = models.OneToOneField('auth.User')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
