# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_count',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('usernum', models.CharField(max_length=50, verbose_name='用户学号')),
                ('count_jidians', models.IntegerField(default=0, verbose_name='个人业绩点')),
            ],
            options={
                'db_table': 'work_count',
                'verbose_name': '业绩点统计',
                'verbose_name_plural': '业绩点统计',
            },
        ),
        migrations.CreateModel(
            name='Work_rate_jidian',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pro_name', models.CharField(max_length=50, verbose_name='职称名')),
                ('scien_jiidans', models.IntegerField(default=0, verbose_name='教学业绩点')),
                ('teach_jiidans', models.IntegerField(default=0, verbose_name='科研业绩点')),
            ],
            options={
                'db_table': 'work_rate_jidian',
                'verbose_name': '职称业绩点',
                'verbose_name_plural': '职称业绩点',
            },
        ),
        migrations.AddField(
            model_name='work_count',
            name='rate_jidians',
            field=models.ForeignKey(verbose_name='额定业绩点', to='teacher.Work_rate_jidian'),
        ),
    ]
