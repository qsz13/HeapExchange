# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0034_auto_20150518_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrangement',
            name='time',
            field=models.DateField(null=True),
        ),
    ]
