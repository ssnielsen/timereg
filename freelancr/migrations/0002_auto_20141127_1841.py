# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=b'N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(default=b'N/A', max_length=255),
        ),
    ]
