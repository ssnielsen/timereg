# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('freelancr', '0002_auto_20141127_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.date(2014, 11, 27)),
            preserve_default=True,
        ),
    ]
