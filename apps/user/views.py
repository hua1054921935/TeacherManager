from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse
import re

from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from apps.user.models import User,Role
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from celery_tasks.tasks import send_mail_register
from utils import xlwt
from .backends import UsernumBackend
# Create your views here.

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        # 1.获取参数
        user_num=request.POST.get('user_num')
        password=request.POST.get('pwd')
        professor=request.POST.get('cpwd')
        email=request.POST.get('email')
        role_id=request.POST.get('loc')
        print(role_id)
        # 2.校验参数完整性
        if not all([user_num,password,professor,email,role_id]):
            return render(request,'register.html',{'errmsg':'数据不完整,请重新输入'})
        # 2.1校验邮箱是否合法
            # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        # 2.2校验用户是否存在
        try:
            user=User.objects.get(user_num=user_num)
        except User.DoesNotExist:
            # 用户不存在
            user=None
        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 3.业务处理,进行注册操作
        role=Role.objects.get(id=role_id)


        user=User()
        user.username=user_num
        user.role=role
        user.professor=professor
        user.email=email
        user.set_password(password)
        user.is_active=0
        user.save()

        # 注册成功需要通过邮箱返回激活链接
        # 使用itsdangerous生成激活的token信息
        seeializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        # 进行加密
        token = seeializer.dumps(info)
        # 转换类型
        token = token.decode()
        # 组织邮件内容
        send_mail_register(email, user_num, token)
        # 返回应答

        # 4.返回响应
        return render(request,'login.html')




 # wbname='新建.xlsx'
#        create_excel(wbname)
#        fields=['姓名','性别','年龄']
#        data=[['1','2','3'],['4','5','6']]
#        shellname='表格1'
#        save_data_excel(data,fields,shellname,wbname)

# 报表导出
class Excel_get(View):
    def get(self,request):
        datas=User.objects.all()
        wbname='全部数据'
        shellname='表格1'
        filelds = ['学工号','邮箱','职称','绩点']
        excel_data=[]
        for data in datas:
            li=[]
            user_num=data.username
            # 获取当前用户的业绩点

            email=data.email
            professor=data.professor
            li.append(user_num)
            li.append(email)
            li.append(professor)
            print(li)
            excel_data.append(li)
        # 创建表格
        # print(excel_data)
        newwbname=xlwt.save_data_excel(excel_data,filelds,shellname,wbname)
        with open(newwbname,'rb') as f:
            excel=f.read()
        response=HttpResponse()
        response['Content-type']='application/vnd.ms-excel'
        response['Content-Disposition'] = 'attachment;filename=user.xlsx'
        response.write(excel)

        return response

class Show_html(View):
    def get(self,request):
        return render(request,'excel.html')



# 登录
class Login(View):
    # 返回登录页面
    def get(self,request):

        return render(request,'login.html')

    def post(self,request):
        # 1.获取参数
        usernum=request.POST.get('usernum')
        pwd=request.POST.get('pwd')
        role_id=request.POST.get('role_id')
        print(usernum,pwd,role_id)

        # 2.校验参数
        if not all([usernum,pwd,role_id]) :
            print('ddddd')
            return render(request,'register.html')
        if role_id=='0':
            return render(request, 'register.html')
        # 3.逻辑处理
        # print(usernum,pwd)
        user=authenticate(username=usernum,password=pwd)
        print(666)
        if user is not None:
        #     return HttpResponse('hello world')
        # else:
        #     return HttpResponse('登录错误')
                # 帐号密码正确
            if user.is_active:
                # 帐号已激活
                # 记住状态
                login(request, user)
                response = redirect(reverse('user:role_select'))
                remember = request.POST.get('remember')

                if remember == 'on':
                    #     记住用户名
                    response.set_cookie('usernum', usernum, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('usernum')
                return response
            else:
                return render(request, 'login.html', {'errmsg': '帐号未激活'})
        else:
            return render(request, 'login.html', {'errmsg': '帐号不存在请注册'})


        # 4.返回响应结果


class Role_select(View):
    def get(self,request):
        user=request.user
        print(user.username)
        print('当前'+str(user.role_id))
        if user.role.role_name=='教师':
            return render(request,'teacheringindex.html')
        elif user.role.role_name=='审核员':
            return render(request,'checker_index.html')
        else:
            return render(request,'adminstor_index.html')
    def post(self,requset):
        pass
# /user/selfmessage


# 个人信息展示
class Usermessage(View):
    def get(self,request):

        user=request.user


        return render(request,'selfmessage.html',{'user':user})
    def post(self,request):
        user_id=request.user.id
        username=request.POST.get('user_name')
        email=request.POST.get('email')
        user=User.objects.get(id=user_id)
        user.username=username
        user.email=email
        user.save()
        return redirect(reverse('user:selfmessage'))


class Loginout(View):
    def get(self,request):
        # user=request.user
        logout(request)
        return redirect(reverse('user:login'))

class ActiveView(View):
    """激活"""
    def get(self, request, token):
        """激活处理"""
        # 进行解密
        serializer = Serializer(settings.SECRET_KEY, 3600)

        try:
            info = serializer.loads(token)

            # 获取待激活用户的id
            user_id = info['confirm']

            # 激活用户
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 返回应答: 跳转到登录页面
            return redirect(reverse('user:login'))
        except Exception as e:
            # 激活链接已失效
            # 实际开发：显示页面告诉用户激活链接已失效，让用户点击链接在发送一封激活邮件
            return HttpResponse('<h1>激活链接已失效</h1>')
