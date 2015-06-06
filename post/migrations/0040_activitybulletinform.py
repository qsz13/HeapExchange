# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0039_auto_20150605_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityBulletinForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initial_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=100, null=True)),
                ('initiator', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(related_name='bulletins', default=1, to='post.Activity')),
            ],
        ),
    ]
