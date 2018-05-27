# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='End_jidna',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('country', models.ForeignKey(verbose_name='组织单位', to='teacher.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_yan',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pro_name', models.CharField(verbose_name='项目名', max_length=50)),
                ('pro_type', models.CharField(verbose_name='项目类别', max_length=50)),
                ('pro_jidian', models.IntegerField(verbose_name='业绩点', default=0)),
                ('pro_discript', models.CharField(verbose_name='备注', max_length=128)),
            ],
            options={
                'verbose_name': '教研业绩',
                'verbose_name_plural': '教研业绩',
                'db_table': 'teacher_yan',
            },
        ),
        migrations.RemoveField(
            model_name='teacher_count',
            name='rate_jidian',
        ),
        migrations.RemoveField(
            model_name='end_pingjia',
            name='pingjia_country',
        ),
        migrations.RemoveField(
            model_name='end_pingjia',
            name='pingjia_jidian',
        ),
        migrations.RemoveField(
            model_name='end_pro',
            name='end_pro_country',
        ),
        migrations.RemoveField(
            model_name='end_pro',
            name='end_pro_jidian',
        ),
        migrations.AlterField(
            model_name='book_auth',
            name='auth_jidian',
            field=models.IntegerField(verbose_name='业绩点', default=0),
        ),
        migrations.AlterField(
            model_name='book_level',
            name='book_jidian',
            field=models.IntegerField(verbose_name='业绩点', default=0),
        ),
        migrations.DeleteModel(
            name='Rate_jidian',
        ),
        migrations.DeleteModel(
            name='Teacher_count',
        ),
    ]
