# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0038_activityimages_courseimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityimages',
            name='activity',
            field=models.ForeignKey(related_name='images', to='post.Activity', null=True),
        ),
        migrations.AlterField(
            model_name='activityimages',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'imgs'),
        ),
        migrations.AlterField(
            model_name='courseimages',
            name='course',
            field=models.ForeignKey(related_name='images', to='post.Course', null=True),
        ),
        migrations.AlterField(
            model_name='courseimages',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'imgs'),
        ),
    ]
