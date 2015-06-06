# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_auto_20150502_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='flag',
            field=models.CharField(default=b'a', max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='flag',
            field=models.CharField(default=b'c', max_length=1),
        ),
    ]
