from django.contrib.auth.models import AbstractUser
from django.db import models

from db.base_model import BaseModel


# Create your models here.
class User(AbstractUser):
    """用户模型类"""
    professor=models.CharField(max_length=20,verbose_name='教师职称')
    user_num=models.CharField(max_length=15,verbose_name='教师工号 ')
    role=models.ForeignKey('Role',verbose_name='所属角色')

    # def __str__(self):
    #     return self.role_name
    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Role(models.Model):
    '''用户角色类'''
    role_name=models.CharField(max_length=10,verbose_name='角色名称')

    def __str__(self):
        return self.role_name
    class Meta:
        db_table='df_role'
        verbose_name='角色名'
        verbose_name_plural=verbose_name
