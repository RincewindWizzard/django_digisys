# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uebungen', '0006_auto_20141029_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=2000, verbose_name='Text')),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Anwesenheitsliste',
            fields=[
            ],
            options={
                'verbose_name': 'Anwesenheitsliste',
                'proxy': True,
                'verbose_name_plural': 'Anwesenheitsliste',
            },
            bases=('uebungen.student',),
        ),
        migrations.CreateModel(
            name='DetailStudent',
            fields=[
            ],
            options={
                'verbose_name': 'Punkte',
                'proxy': True,
                'verbose_name_plural': 'Punkte',
            },
            bases=('uebungen.student',),
        ),
        migrations.RemoveField(
            model_name='student',
            name='klausur_points',
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Vorname'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Nachname'),
            preserve_default=True,
        ),
    ]
