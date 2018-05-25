from django.test import TestCase
# from django.contrib.auth.models import User
from apps.user.models import Role,User
# Create your tests here.
role=Role.objects.get(id=3)
print(role.role_name)
user=User.objects.create_superuser('admin',123456,role)

print('wanchneg')