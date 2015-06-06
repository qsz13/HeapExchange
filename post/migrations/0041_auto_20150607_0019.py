# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0040_activitybulletinform'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityBulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initial_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=100, null=True)),
                ('initiator', models.ForeignKey(related_name='activity_bulletins', default=1, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(related_name='bulletins', default=1, to='post.Activity')),
            ],
        ),
        migrations.RemoveField(
            model_name='activitybulletinform',
            name='initiator',
        ),
        migrations.RemoveField(
            model_name='activitybulletinform',
            name='post',
        ),
        migrations.AlterField(
            model_name='coursebulletin',
            name='initiator',
            field=models.ForeignKey(related_name='course_bulletins', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ActivityBulletinForm',
        ),
    ]
