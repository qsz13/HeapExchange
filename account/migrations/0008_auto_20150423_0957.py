# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awesome_avatar.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20150423_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=awesome_avatar.fields.AvatarField(default=b'default.png', upload_to=b'avatar'),
        ),
    ]
