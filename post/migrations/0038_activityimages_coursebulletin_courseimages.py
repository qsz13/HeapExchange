# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0037_auto_20150602_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(null=True, upload_to=b'imgs')),
                ('post', models.ForeignKey(related_name='images', to='post.Activity', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseBulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initial_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=100, null=True)),
                ('initiator', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(related_name='bulletins', default=1, to='post.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(null=True, upload_to=b'imgs')),
                ('post', models.ForeignKey(related_name='images', to='post.Course', null=True)),
            ],
        ),
    ]
