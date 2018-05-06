from django.test import TestCase
# from django.contrib.auth.models import User
from apps.user.models import Role,User
# Create your tests here.
role=Role.objects.get(id=1)
user=User.objects.create_superuser(username='admin',password=123456,role=role)