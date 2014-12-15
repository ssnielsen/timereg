# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('freelancr', '0004_activity_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='billed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='payed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.date(2014, 12, 2)),
        ),
    ]
