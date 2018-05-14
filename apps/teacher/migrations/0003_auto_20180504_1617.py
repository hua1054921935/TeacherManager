# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20180504_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate_jidian',
            name='jiidan',
        ),
        migrations.AddField(
            model_name='rate_jidian',
            name='scien_jidian',
            field=models.FloatField(verbose_name='科研额定绩点', default=0),
        ),
        migrations.AddField(
            model_name='rate_jidian',
            name='teach_jidian',
            field=models.IntegerField(verbose_name='教学额定绩点', default=0),
        ),
    ]
