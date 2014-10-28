# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uebungen', '0003_auto_20141028_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Student', 'verbose_name_plural': 'Studenten'},
        ),
        migrations.AlterField(
            model_name='abgabe',
            name='points',
            field=models.IntegerField(verbose_name='Punkte'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extrapunkte',
            name='points',
            field=models.IntegerField(verbose_name='Punkte'),
            preserve_default=True,
        ),
    ]
