# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_auth',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('book_auth_name', models.CharField(verbose_name='主编名称', max_length=50)),
                ('auth_jidian', models.IntegerField(default=0, verbose_name='业绩点')),
            ],
            options={
                'verbose_name_plural': '主编部分',
                'db_table': 'book_auth',
                'verbose_name': '主编部分',
            },
        ),
        migrations.CreateModel(
            name='Book_level',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('book_level_name', models.CharField(verbose_name='等级名称', max_length=50)),
                ('book_jidian', models.IntegerField(default=0, verbose_name='业绩点')),
            ],
            options={
                'verbose_name_plural': '教材级别系数、语言类别系数表',
                'db_table': 'book_level',
                'verbose_name': '教材级别系数、语言类别系数表',
            },
        ),
        migrations.CreateModel(
            name='Book_lixiang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('book_lixiang_name', models.CharField(verbose_name='立项名', max_length=50)),
                ('book_lixiang_math', models.CharField(verbose_name='立项系数', max_length=50)),
            ],
            options={
                'verbose_name_plural': '立项系数',
                'db_table': 'book_lixiang',
                'verbose_name': '立项系数',
            },
        ),
        migrations.CreateModel(
            name='Rate_jidian',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='职称名', max_length=50)),
                ('scien_jiidan', models.IntegerField(default=0, verbose_name='教学业绩点')),
                ('teach_jiidan', models.IntegerField(default=0, verbose_name='科研业绩点')),
            ],
            options={
                'verbose_name_plural': '职称对应业绩点',
                'db_table': 'rate_jidian',
                'verbose_name': '职称对应业绩点',
            },
        ),
        migrations.CreateModel(
            name='Teacher_book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('book_auth', models.ForeignKey(to='teacher.Book_auth', verbose_name='主编部分')),
                ('book_level', models.ForeignKey(to='teacher.Book_level', verbose_name='.教材级别系数、语言类别系数表')),
                ('book_lixiang', models.ForeignKey(to='teacher.Book_lixiang', verbose_name='立项系数')),
            ],
            options={
                'verbose_name_plural': '教材业绩量化表',
                'db_table': 'teacher_book',
                'verbose_name': '教材业绩量化表',
            },
        ),
        migrations.CreateModel(
            name='Teacher_count',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('usernum', models.CharField(verbose_name='用户学号', max_length=50)),
                ('count_jidian', models.IntegerField(default=0, verbose_name='个人业绩点')),
                ('rate_jidian', models.ForeignKey(to='teacher.Rate_jidian', verbose_name='额定业绩点')),
            ],
            options={
                'verbose_name_plural': '教师业绩点统计',
                'db_table': 'teacher_count',
                'verbose_name': '教师业绩点统计',
            },
        ),
        migrations.CreateModel(
            name='Teacher_pingtai',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pro_level', models.CharField(verbose_name='项目级别', max_length=50)),
                ('pro_huozhun', models.IntegerField(default=0, verbose_name='获准业绩点')),
                ('pro_huozhunlast', models.IntegerField(default=0, verbose_name='获准后建设期年度考核业绩点')),
                ('pro_check', models.CharField(verbose_name='考核等级', max_length=128)),
                ('pro_check_math', models.CharField(verbose_name='考核等级', max_length=128)),
            ],
            options={
                'verbose_name_plural': '教学平台建设业绩量化表',
                'db_table': 'teacher_pingtai',
                'verbose_name': '教学平台建设业绩量化表',
            },
        ),
        migrations.CreateModel(
            name='Teacher_work',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(verbose_name='课程名', max_length=50)),
                ('course_type', models.CharField(verbose_name='课程类别', max_length=50)),
                ('course_jidian', models.IntegerField(default=0, verbose_name='业绩点')),
                ('course_discript', models.CharField(verbose_name='描述', max_length=128)),
            ],
            options={
                'verbose_name_plural': '教学工作量业绩',
                'db_table': 'teacher_work',
                'verbose_name': '教学工作量业绩',
            },
        ),
        migrations.CreateModel(
            name='Teacher_yan',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(verbose_name='项目名', max_length=50)),
                ('pro_type', models.CharField(verbose_name='项目类别', max_length=50)),
                ('pro_jidian', models.IntegerField(default=0, verbose_name='业绩点')),
                ('pro_discript', models.CharField(verbose_name='备注', max_length=128)),
            ],
            options={
                'verbose_name_plural': '教研业绩',
                'db_table': 'teacher_yan',
                'verbose_name': '教研业绩',
            },
        ),
    ]
