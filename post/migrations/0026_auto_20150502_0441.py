# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_auto_20150502_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='flag',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='activity',
            name='limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='flag',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.IntegerField(null=True),
        ),
    ]
