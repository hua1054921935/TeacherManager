from django.contrib import admin
from utils.matlib import read_xls
from .models import User,Role,ImportFile


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

class ImportFileAdmin(admin.ModelAdmin):
    list_display = ['id','file','name']
    # fields = ('file','name')
    list_filter = ['name', ]
    def save_model(self, request, obj, form, change):
        re = super(ImportFileAdmin, self).save_model(request, obj, form, change)
        data=read_xls(self,request, obj, change)
        print(data)
        return re

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(ImportFile,ImportFileAdmin)