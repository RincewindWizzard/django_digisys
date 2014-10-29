# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uebungen', '0005_student_klausur_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='klausur_points',
            field=models.IntegerField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
