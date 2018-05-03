from django.db import models

# Create your models here.
class Teacher_work(models.Model):
    course_name=models.CharField(max_length=50,verbose_name='课程名')
    course_type=models.CharField(max_length=50,verbose_name='课程类别')
    course_jidian=models.IntegerField(default=0,verbose_name='业绩点')
    course_discript=models.CharField(max_length=128,verbose_name='课程名')

