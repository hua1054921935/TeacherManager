# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20180505_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('country_name', models.CharField(verbose_name='组织单位名', max_length=120)),
            ],
            options={
                'verbose_name': '组织单位',
                'verbose_name_plural': '组织单位',
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='End_pingjia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pingjia_name', models.CharField(verbose_name='评价等级', max_length=120)),
                ('pingjia_jidian', models.CharField(verbose_name='对应绩点', max_length=120)),
                ('pingjia_country', models.ForeignKey(verbose_name='对应单位', to='teacher.Country')),
            ],
            options={
                'verbose_name': '评价',
                'verbose_name_plural': '评价',
                'db_table': 'end_pingjia',
            },
        ),
        migrations.CreateModel(
            name='End_pro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('end_pro_name', models.CharField(verbose_name='结题等级', max_length=120)),
                ('end_pro_jidian', models.CharField(verbose_name='对应绩点', max_length=120)),
                ('end_pro_country', models.ForeignKey(verbose_name='对应单位', to='teacher.Country')),
            ],
            options={
                'verbose_name': '结题',
                'verbose_name_plural': '结题',
                'db_table': 'end_pro',
            },
        ),
        migrations.CreateModel(
            name='Intellectual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('intellectual_name', models.CharField(verbose_name='专利名称', max_length=120)),
                ('intellectual_jidina', models.CharField(verbose_name='专利绩点', max_length=120)),
            ],
            options={
                'verbose_name': '知识产权',
                'verbose_name_plural': '知识产权',
                'db_table': 'intellectual',
            },
        ),
        migrations.CreateModel(
            name='Kaohe_level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('kaohe_name', models.CharField(verbose_name='考核验收等级名', max_length=120)),
                ('kaohe_math', models.CharField(verbose_name='考核验收系数', max_length=120)),
            ],
            options={
                'verbose_name': '考核验收等级',
                'verbose_name_plural': '考核验收等级',
                'db_table': ' kaohe_level',
            },
        ),
        migrations.CreateModel(
            name='Nature_keyan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pro_level', models.CharField(verbose_name='项目级别', max_length=120)),
                ('pro_math', models.CharField(verbose_name='系数', max_length=20)),
                ('pro_jidian', models.CharField(verbose_name='立项绩点', max_length=120)),
            ],
            options={
                'verbose_name': '自然科学 科研项目业绩量化',
                'verbose_name_plural': '自然科学 科研项目业绩量化',
                'db_table': 'nature_keyan',
            },
        ),
        migrations.CreateModel(
            name='Nut_book_auth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('book_auth_name', models.CharField(verbose_name='著书身份名', max_length=120)),
                ('book_auth_jidian', models.CharField(verbose_name='对应业绩点', max_length=120)),
            ],
            options={
                'verbose_name': '著书身份',
                'verbose_name_plural': '著书身份',
                'db_table': 'nut_book_auth',
            },
        ),
        migrations.CreateModel(
            name='Nut_book_concern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('book_concern_name', models.CharField(verbose_name='出版社级别名', max_length=120)),
                ('book_concern_jidian', models.CharField(verbose_name='对应系数', max_length=120)),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
                'db_table': 'nut_book_concern',
            },
        ),
        migrations.CreateModel(
            name='Nut_book_lixinag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('book_lixinag_name', models.CharField(verbose_name='立项名', max_length=120)),
                ('book_lixinag_jidian', models.CharField(verbose_name='对应系数', max_length=120)),
            ],
            options={
                'verbose_name': '立项',
                'verbose_name_plural': '立项',
                'db_table': 'nut_book_lixinag',
            },
        ),
        migrations.CreateModel(
            name='Pingtai',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pingtai_huozhun', models.CharField(verbose_name='获准绩点', max_length=120)),
                ('pingtai_yanshou', models.CharField(verbose_name='验收绩点', max_length=120)),
                ('pingtai_level', models.ForeignKey(verbose_name='等级', to='teacher.Country')),
            ],
            options={
                'verbose_name': '科研平台',
                'verbose_name_plural': '科研平台',
                'db_table': 'pingtai',
            },
        ),
        migrations.CreateModel(
            name='Reward_level1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('reward_level1_name', models.CharField(verbose_name='奖励等级1名', max_length=120)),
            ],
            options={
                'verbose_name': '奖励等级1',
                'verbose_name_plural': '奖励等级1',
                'db_table': 'reward_level1',
            },
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('reward_jidian', models.CharField(verbose_name='奖励绩点', max_length=120)),
                ('reward_level', models.ForeignKey(verbose_name='奖励等级', to='teacher.Country')),
                ('reward_level1', models.ForeignKey(verbose_name='奖励等级1', to='teacher.Reward_level1')),
            ],
            options={
                'verbose_name': '科研奖励',
                'verbose_name_plural': '科研奖励',
                'db_table': 'science',
            },
        ),
        migrations.CreateModel(
            name='Thesis_cscd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cscd_name', models.CharField(verbose_name='cscd核心库', max_length=120)),
                ('cscd_jidian', models.CharField(verbose_name='对应业绩点', max_length=120)),
            ],
            options={
                'verbose_name': 'cscd区',
                'verbose_name_plural': 'cscd区',
                'db_table': 'thesis_cscd',
            },
        ),
        migrations.CreateModel(
            name='Thesis_ei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ei_name', models.CharField(verbose_name='ei收录', max_length=120)),
                ('ei_jidian', models.CharField(verbose_name='对应业绩点', max_length=120)),
            ],
            options={
                'verbose_name': 'ei区',
                'verbose_name_plural': 'ei区',
                'db_table': 'thesis_ei',
            },
        ),
        migrations.CreateModel(
            name='Thesis_sci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sci_name', models.CharField(verbose_name='sci收录', max_length=120)),
                ('sci_jidian', models.CharField(verbose_name='对应业绩点', max_length=120)),
            ],
            options={
                'verbose_name': 'sci区',
                'verbose_name_plural': 'sci区',
                'db_table': 'thesis_sci',
            },
        ),
    ]
