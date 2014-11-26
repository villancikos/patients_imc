# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_auto_20141124_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_fum',
            field=models.DateField(default=datetime.date(2014, 11, 24), help_text=b'FUM = Fecha de Ultima Menstruacion'),
            preserve_default=False,
        ),
    ]
