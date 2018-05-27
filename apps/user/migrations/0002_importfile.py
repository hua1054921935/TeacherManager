# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('file', models.FileField(upload_to='File')),
                ('name', models.CharField(verbose_name='文件名', max_length=50)),
            ],
            options={
                'verbose_name': '批量导入用户',
                'ordering': ['name'],
                'verbose_name_plural': '批量导入用户',
            },
        ),
    ]
