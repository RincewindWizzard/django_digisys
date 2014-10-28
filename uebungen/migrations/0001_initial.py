# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abgabe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.IntegerField(choices=[(1, b'Serie 1'), (2, b'Serie 2'), (3, b'Serie 3'), (4, b'Serie 4'), (5, b'Serie 5'), (6, b'Serie 6'), (7, b'Serie 7'), (8, b'Serie 8'), (9, b'Serie 9'), (10, b'Serie 10'), (11, b'Serie 11'), (12, b'Serie 12')])),
                ('points', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Extrapunkte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kolloquium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('points', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('matrikel', models.IntegerField()),
                ('stu_mail', models.EmailField(max_length=75)),
                ('mail', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Uebung',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('anwesenheit', models.ManyToManyField(to='uebungen.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kolloquium',
            name='student',
            field=models.ForeignKey(to='uebungen.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extrapunkte',
            name='student',
            field=models.ForeignKey(to='uebungen.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extrapunkte',
            name='uebung',
            field=models.ForeignKey(to='uebungen.Uebung'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abgabe',
            name='student_A',
            field=models.ForeignKey(related_name='abgabe_a', to='uebungen.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abgabe',
            name='student_B',
            field=models.ForeignKey(related_name='abgabe_b', to='uebungen.Student'),
            preserve_default=True,
        ),
    ]
