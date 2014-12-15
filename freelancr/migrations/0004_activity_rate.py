# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancr', '0003_activity_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
