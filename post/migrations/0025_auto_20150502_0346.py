# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20150502_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateField(null=True),
        ),
    ]
