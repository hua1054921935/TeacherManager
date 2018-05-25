# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher_yan',
        ),
        migrations.AlterField(
            model_name='book_auth',
            name='auth_jidian',
            field=models.FloatField(default=0, verbose_name='业绩点'),
        ),
        migrations.AlterField(
            model_name='book_level',
            name='book_jidian',
            field=models.FloatField(default=0, verbose_name='业绩点'),
        ),
    ]
