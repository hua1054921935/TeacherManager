from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Teacher_work,Teacher_pingtai,Book_level,Book_lixiang,Book_auth,Teacher_count,Rate_jidian
# Create your views here.
# 教师业绩量化

class Teacher_selcet(View):
    def get(self,request):
        user=request.user
        username=user.username
    #     获取该老师对应的业绩信息
        teacher_count=Teacher_count.objects.filter(usernum=username)
        for data in teacher_count:
            count=count+data.count_jidian

    def post(self,request):
        pass


# 教研业绩
class Teachers_yan(View):

    def get(self,request):
        data_list=Teacher_work.objects.all()
        return render(request,'teachering.html',{'data_list':data_list})
    def post(self,request):
        pass
# 教学平台业绩量化
class Teachers_pingtai(View):
    def get(self,request):
        data_list = Teacher_pingtai.objects.all()
        return render(request, 'teachering_result.html', {'data_list': data_list})
    def post(self,request):
        pass

# 教材业绩量化
class Teachers_book(View):
    def get(self,request):
        dict1={}
        # 获取教材级别系数、语言类别系数表Book_level
        book_levels = Book_level.objects.all()
        dict1['book_levels']=book_levels
        # 主编部分
        book_auths=Book_auth.objects.all()
        dict1['book_auths']=book_auths
        # 立项系数
        book_lixiangs=Book_lixiang.objects.all()
        dict1['book_lixiangs']=book_lixiangs

        return render(request, 'teachering_book.html', {'dict1':dict1})
    # post请求处理数据
    def post(self,request):
        # 获取到对应的id、
        user=request.user
        book_level=request.POST.get('book_level')
        book_auth=request.POST.get('book_auth')
        book_lixiang=request.POST.get('lixiang')
        book_mount=float(request.POST.get('book_mount'))
        zaiban_math=float(request.POST.get('zaiban_math'))
        # 获取对应的业绩点

        book_level_math=float(Book_level.objects.get(id=book_level).book_jidian)
        book_auth_jidian=float(Book_auth.objects.get(id=book_auth).auth_jidian)
        book_lixiang_maths=float(Book_lixiang.objects.get(id=book_lixiang).book_lixiang_math)
        if zaiban_math:
            zaiban_math=zaiban_math
        else:
            zaiban_math=1

        book_count=book_auth_jidian*book_mount*book_level_math*book_lixiang_maths*zaiban_math
        # 存入对应的业绩表中
        username=user.username
        professor=user.professor
        rate_jidian=Rate_jidian.objects.get(name=professor)
        teacher_count=Teacher_count()
        Teacher_count.objects.create(usernum=username,count_jidian=book_count,rate_jidian=rate_jidian)


        return HttpResponse('ok')
        # print(book1_jidian)
        # print(book_level,book_auth,book_lixiang,book_mount)
