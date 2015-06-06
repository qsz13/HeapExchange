# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_auto_20150507_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrangement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(null=True)),
                ('content', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('post', models.ForeignKey(related_name='arrangement', default=1, to='post.Course')),
            ],
        ),
    ]
