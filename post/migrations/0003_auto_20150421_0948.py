# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20150413_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'DEFAULT', max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 9, 48, 58, 149111))),
                ('description', models.CharField(default=b'DEFAULT', max_length=500)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 9, 48, 58, 149215))),
                ('location', models.CharField(default=b'DEFAULT', max_length=100)),
                ('requirement', models.CharField(default=b'DEFAULT', max_length=500)),
                ('initialtime', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 9, 48, 58, 149318))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='post',
            name='flag_user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='link',
        ),
        migrations.RemoveField(
            model_name='course',
            name='place',
        ),
        migrations.RemoveField(
            model_name='course',
            name='skill_requirement',
        ),
        migrations.RemoveField(
            model_name='course',
            name='student_limit',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 9, 48, 58, 149215)),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default=b'DEFAULT', max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 9, 48, 58, 149318)),
        ),
        migrations.AddField(
            model_name='course',
            name='joined',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.CharField(default=b'DEFAULT', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='requirement',
            field=models.CharField(default=b'DEFAULT', max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 9, 48, 58, 149111)),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default=b'DEFAULT', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
