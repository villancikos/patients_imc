# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='modified_date',
            field=models.DateField(default=datetime.date(2014, 11, 24), auto_now=True),
            preserve_default=False,
        ),
    ]
