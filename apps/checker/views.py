from django.shortcuts import render,redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from apps.teacher.models import Work_count
from apps.user.models import User
from apps.teacher.models import Work_rate_jidian
from utils import xlwt
from django.http import HttpResponse
# Create your views here.


class Scinece(View):
    def get(self,request):
        pass
    def post(self,request):
        pass


class ShowData(View):
    def get(self, request):
        # 1.获取所有教职工信息
        user = User.objects.all()
        #     2.获取职工的业绩
        dict1 = {}
        list1 = []
        list2 = []
        for data in user:
            username = data.id
            user_num=data.username
            list1.append(int(user_num))

            teacher_count = Work_count.objects.filter(usernum=username)
            data = 0
            for count in teacher_count:
                data = data + count.count_jidians
            list2.append(data)
        dict1['username'] = list1
        dict1['jiidan'] = list2

        return render(request, 'checker_data.html', dict1)
    def post(self):
        pass


class Cherker_index(View):
    def get(self, request):
        return render(request, 'checker_index.html')


class Checker_message(View):
    def get(self,request):

        user=request.user


        return render(request,'checker_message.html',{'user':user})
    def post(self,request):
        user_id=request.user.id
        username=request.POST.get('user_name')
        email=request.POST.get('email')
        user=User.objects.get(id=user_id)
        user.username=username
        user.email=email
        user.save()
        return redirect(reverse('checker:checker_message'))


class Checker_select_all(View):
    def get(self,request):

        user = User.objects.all()
        list1=[]
        for data in user:

            dict1 = {}
            dict1['username'] = data.username  # 获取该老师对应的业绩信息
            teacher_count = Work_count.objects.filter(usernum=data.id)

            count = 0
            for data in teacher_count:
                count = count + data.count_jidians
                rate_jidian = data.rate_jidians
                dict1['teacher_jidian'] = rate_jidian.teach_jiidans
                dict1['secien_jidian'] = rate_jidian.scien_jiidans
            dict1['count'] = count
            list1.append(dict1)
        return render(request, 'checker_select_all.html', {'list1': list1})
    def post(self,request):
        pass

class Checker_shehe(View):
    def get(self,request,username):
        print(username)
        user=User.objects.get(username=username)
        dict1 = {}
        dict1['username'] = username  # 获取该老师对应的业绩信息
        teacher_count = Work_count.objects.filter(usernum=user.id)
        count = 0
        for data in teacher_count:
            count = count + data.count_jidians
            rate_jidian = data.rate_jidians
            dict1['teacher_jidian'] = rate_jidian.teach_jiidans
            dict1['secien_jidian'] = rate_jidian.scien_jiidans
        dict1['count'] = count
        return render(request, 'checker_shenhe.html', {'data': dict1})

    def post(self,request,das):
        username=request.POST.get('user_name')
        print(username)
        book_count=request.POST.get('pwd')
        user=User.objects.get(username=username)

        rate_jidians = Work_rate_jidian.objects.get(pro_name=user.professor)
        data=Work_count.objects.filter(usernum=user.id)
        if data:
            data.update(usernum=user.id,count_jidians=book_count, rate_jidians=rate_jidians)
        else:
            data.create(usernum=user.id, count_jidians=book_count, rate_jidians=rate_jidians)
        return redirect(reverse('checker:checker_select_all'))


class Excel_get(View):
    def get(self, request):
        datas = User.objects.all()
        wbname = '全部数据'
        shellname = '表格1'
        filelds = ['学工号', '邮箱', '职称', '绩点']
        excel_data = []
        for data in datas:
            li = []
            user_num = data.username
            # 获取所有用户的业绩点
            try:
                teacher_count = Work_count.objects.get(usernum=data.id)
                email = data.email
                professor = data.professor
                li.append(user_num)
                li.append(email)
                li.append(professor)
                li.append(teacher_count.count_jidians)
            except Exception as e:
                print(e)




            print(li)
            excel_data.append(li)
        # 创建表格
        # print(excel_data)
        newwbname = xlwt.save_data_excel(excel_data, filelds, shellname, wbname)
        with open(newwbname, 'rb') as f:
            excel = f.read()
        response = HttpResponse()
        response['Content-type'] = 'application/vnd.ms-excel'
        response['Content-Disposition'] = 'attachment;filename=user.xlsx'
        response.write(excel)

        return response