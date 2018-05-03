from django.db import models
from apps.user.models import User
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
    # book_level=models.SmallIntegerField(default=1,choices=Choice,verbose_name='1.教材级别系数、语言类别系数表')
    book_level=models.ForeignKey('Book_level',verbose_name='.教材级别系数、语言类别系数表')
    book_auth=models.ForeignKey('Book_auth',verbose_name='主编部分')
    book_lixiang=models.ForeignKey('Book_lixiang',verbose_name='立项系数')
    class Meta:
        db_table = 'teacher_book'
        verbose_name = '教材业绩量化表'
        verbose_name_plural = verbose_name


class Book_level(models.Model):
    book_level_name=models.CharField(max_length=50, verbose_name='等级名称')
    book_jidian=models.IntegerField(default=0, verbose_name='业绩点')
    class Meta:
        db_table = 'book_level'
        verbose_name = '教材级别系数、语言类别系数表'
        verbose_name_plural = verbose_name
class Book_auth(models.Model):
    book_auth_name = models.CharField(max_length=50, verbose_name='主编名称')
    auth_jidian = models.IntegerField(default=0, verbose_name='业绩点')

    class Meta:
        db_table = 'book_auth'
        verbose_name = '主编部分'
        verbose_name_plural = verbose_name
class Book_lixiang(models.Model):
    book_lixiang_name = models.CharField(max_length=50, verbose_name='立项名')
    book_lixiang_math = models.CharField(max_length=50, verbose_name='立项系数')

    class Meta:
        db_table = 'book_lixiang'
        verbose_name = '立项系数'
        verbose_name_plural = verbose_name



# 业绩表
class Teacher_count(models.Model):
    usernum=models.CharField(max_length=50,verbose_name='用户学号')
    count_jidian=models.IntegerField(default=0,verbose_name='个人业绩点')
    rate_jidian=models.ForeignKey('Rate_jidian',verbose_name='额定业绩点')
    class Meta:
        db_table = 'teacher_count'
        verbose_name = '教师业绩点统计'
        verbose_name_plural = verbose_name

class Rate_jidian(models.Model):
    name=models.CharField(max_length=50, verbose_name='职称名')
    jiidan=models.IntegerField(default=0,verbose_name='职称对应业绩点')
    class Meta:
        db_table = 'rate_jidian'
        verbose_name = '职称对应业绩点'
        verbose_name_plural = verbose_name