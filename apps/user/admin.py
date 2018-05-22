from django.contrib import admin

from .models import User, Role


# Register your models here.
# role=Role.objects.get(id=3)
# user=User.objects.create_superuser(username=201400830000,password='123456',email='hua1054921935@si9na.com',role=role)
# user.save()
# admin.site.register([User,Role])

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'professor', 'email', 'role']
    fields = ('username', 'professor', 'email', 'role')


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name']


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
