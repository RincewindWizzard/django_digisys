# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uebungen', '0004_auto_20141028_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='klausur_points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
