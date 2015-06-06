# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True, verbose_name='\u5e74\u9f84', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=None, max_length=1, null=True, verbose_name='\u6027\u522b', choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=13, null=True, verbose_name='\u7535\u8bdd', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(max_length=15, null=True, verbose_name='\u5b66\u9662', blank=True),
        ),
    ]
