# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_requirement', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('student_limit', models.IntegerField()),
                ('price', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField()),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('flag_times', models.IntegerField(null=True)),
                ('creator', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('flag_user', models.ManyToManyField(related_name='flag_post', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.ManyToManyField(to='post.Tag'),
        ),
    ]
