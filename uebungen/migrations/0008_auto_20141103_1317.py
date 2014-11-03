# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uebungen', '0007_auto_20141029_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notiz',
            options={'verbose_name': 'Notiz', 'verbose_name_plural': 'Notizen'},
        ),
    ]
