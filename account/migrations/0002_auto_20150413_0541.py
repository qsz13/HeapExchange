# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=13, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='timetable',
            field=models.CharField(default=b'00000000000000000000000000000000000000000000000000000000000000000000000000000', max_length=77),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=None, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
