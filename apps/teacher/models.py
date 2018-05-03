from django.db import models

# Create your models here.
# 教学工作量
class Teacher_work(models.Model):
    course_name=models.CharField(max_length=50,verbose_name='课程名')
    course_type=models.CharField(max_length=50,verbose_name='课程类别')
    course_jidian=models.IntegerField(default=0,verbose_name='业绩点')
    course_discript=models.CharField(max_length=128,verbose_name='描述')
    class Meta:
        db_table = 'teacher_work'
        verbose_name = '教学工作量业绩'
        verbose_name_plural = verbose_name
# 教研业绩量化
class Teacher_yan(models.Model):
    pro_name = models.CharField(max_length=50, verbose_name='项目名')
    pro_type = models.CharField(max_length=50, verbose_name='项目类别')
    pro_jidian = models.IntegerField(default=0, verbose_name='业绩点')
    pro_discript = models.CharField(max_length=128, verbose_name='备注')
    class Meta:
        db_table = 'teacher_yan'
        verbose_name = '教研业绩'
        verbose_name_plural = verbose_name

# 教学平台建设业绩量化表
class Teacher_pingtai(models.Model):
    pro_level = models.CharField(max_length=50, verbose_name='项目级别')
    pro_huozhun = models.IntegerField(default=0, verbose_name='获准业绩点')
    pro_huozhunlast = models.IntegerField(default=0, verbose_name='获准后建设期年度考核业绩点')
    pro_check = models.CharField(max_length=128, verbose_name='考核等级')
    pro_check_math = models.CharField(max_length=128, verbose_name='考核等级')

    class Meta:
        db_table = 'teacher_pingtai'
        verbose_name = '教学平台建设业绩量化表'
        verbose_name_plural = verbose_name

# 教材业绩量化表
class Teacher_book(models.Model):
    Choice=((0,'国家级规划教材'),
            (1,'省级规划教材'),
            (2, '其他教材'),
            (3, '中文编写'),
            (4, '外文编写')
            )
    book_level=models.SmallIntegerField(default=1,choices=Choice,verbose_name='1.教材级别系数、语言类别系数表')
