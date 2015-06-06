# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0038_activityimages_courseimages'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='activityimages',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='courseimages',
            name='course',
        ),
        migrations.AddField(
            model_name='activityimages',
            name='post',
            field=models.ForeignKey(related_name='images', to='post.Activity', null=True),
        ),
        migrations.AddField(
            model_name='courseimages',
            name='post',
            field=models.ForeignKey(related_name='images', to='post.Course', null=True),
        ),
        migrations.AlterField(
            model_name='activityimages',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'imgs'),
        ),
        migrations.AlterField(
            model_name='courseimages',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'imgs'),
        ),
    ]
