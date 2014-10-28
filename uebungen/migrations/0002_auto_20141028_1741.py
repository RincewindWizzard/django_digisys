# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uebungen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abgabe',
            options={'verbose_name': 'Abgabe', 'verbose_name_plural': 'Abgaben'},
        ),
        migrations.AlterModelOptions(
            name='extrapunkte',
            options={'verbose_name': 'Extrapunkte', 'verbose_name_plural': 'Extrapunkte'},
        ),
        migrations.AlterModelOptions(
            name='kolloquium',
            options={'verbose_name': 'Kolloquium', 'verbose_name_plural': 'Kolloquien'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Studenten'},
        ),
        migrations.AlterModelOptions(
            name='uebung',
            options={'verbose_name': '\xdcbung', 'verbose_name_plural': '\xdcbungen'},
        ),
        migrations.AlterField(
            model_name='kolloquium',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='mail',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uebung',
            name='anwesenheit',
            field=models.ManyToManyField(to='uebungen.Student', verbose_name='Anwesenheit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uebung',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
