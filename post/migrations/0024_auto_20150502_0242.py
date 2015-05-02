# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20150502_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='flag',
            field=models.CharField(default=b'a', max_length=1),
        ),
    ]
