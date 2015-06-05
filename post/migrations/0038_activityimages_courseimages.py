# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0037_auto_20150602_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'')),
                ('activity', models.ForeignKey(related_name='images', to='post.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='CourseImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'')),
                ('course', models.ForeignKey(related_name='images', to='post.Course')),
            ],
        ),
    ]
