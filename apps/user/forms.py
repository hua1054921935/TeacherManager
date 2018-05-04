# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):   # 定义创建登录用户和超级用户时需要的字段
    def create_user(self, email, user_num, professor,role,password=None):
        print(66666666)
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_num:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_num=user_num,
            role=role,
            professor=professor
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

