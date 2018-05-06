from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View
from .models import Teacher_work,Teacher_pingtai,Book_level,Book_lixiang,Book_auth,Work_rate_jidian,Work_count,Nature_keyan,Thesis_sci,Thesis_cscd,Thesis_ei,Intellectual

# Create your views here.
# 教师业绩量化

class Teacher_selcet(View):
    def get(self,request):
        user=request.user
        username=user.username
        dict1 = {}
        dict1['username']=username    #     获取该老师对应的业绩信息
        teacher_count=Work_count.objects.filter(usernum=username)

        count=0
        for data in teacher_count:
            count=count+data.count_jidians
            rate_jidian=data.rate_jidians
            dict1['teacher_jidian']=rate_jidian.teach_jiidans
            dict1['secien_jidian']=rate_jidian.scien_jiidans
        dict1['count']=count

        return render(request,'teachering_select.html',{'data':dict1})
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

        rate_jidians=Work_rate_jidian.objects.get(pro_name=professor)

        # teacher_count=Teacher_count()
        Work_count.objects.create(usernum=username,count_jidians=book_count,rate_jidians=rate_jidians)


        return redirect(reverse('teacher:teachers_selcet'))
        # print(book1_jidian)
        # print(book_level,book_auth,book_lixiang,book_mount)




# 在自然科学 科研项目业绩量化
class Teachers_science(View):
    def get(self,request):
        data_list=Nature_keyan.objects.all()
        return render(request, 'teachering_secience.html', {'data_list': data_list})
    def post(self,request):
        pass
#论文
class Teachers_thesis(View):
    def get(self,request):
        # sci收录
        dict2={}
        thesis_sci=Thesis_sci.objects.all()
        dict2['thesis_sci']=thesis_sci
        thesis_cscd=Thesis_cscd.objects.all()
        dict2['thesis_cscd']=thesis_cscd
        thesis_ei=Thesis_ei.objects.all()
        dict2['thesis_ei']=thesis_ei
        return render(request,'teacheringlunwen.html',{'dict2':dict2})

    def post(self,request):
        # 获取到对应的id、
        user = request.user
        sci = request.POST.get('sci')
        ei= request.POST.get('ei')
        natureScience = request.POST.get('natureScience')
        cscd = float(request.POST.get('cscd'))
        auth = float(request.POST.get('auth'))
        # 获取到对应的业绩点
        max_jidna=0
        if natureScience=="1":
            max_jidna=3000
        else:
            max_jidna=0
        if sci:
            sci_jidian=float(Thesis_sci.objects.get(id=sci).sci_jidian)
            if sci_jidian>=max_jidna:
                max_jidna=sci_jidian
            else:
                max_jidna=max_jidna
        if ei:
            ei_jidan=float(Thesis_ei.objects.get(id=ei).ei_jidian)
            if ei_jidan>=max_jidna:
                max_jidna=ei_jidan
            else:
                max_jidna=max_jidna
        if cscd:
            cscd_jidian=float(Thesis_cscd.objects.get(id=cscd).cscd_jidian)
            if cscd_jidian>=max_jidna:
                max_jidna=cscd_jidian
            else:
                max_jidna=max_jidna
        if auth=="1":
            math=1
        else:
            math=0.3
        book_count=max_jidna*math
        username=user.username
        professor = user.professor

        rate_jidians = Work_rate_jidian.objects.get(pro_name=professor)
        Work_count.objects.create(usernum=username, count_jidians=book_count, rate_jidians=rate_jidians)
        return redirect(reverse('teacher:teachers_selcet'))

# 知识产权
class Teachers_chanquan(View):
    def get(self,request):

        # 知识产权表
        data_list=Intellectual.objects.all()
        return  render(request,'teacheringchanquan.html',{'data_list':data_list})
    def post(self,request):
        user=request.user
        # 获取对应的绩点
        intellectuals_name=request.POST.get('intellectual_name')
        math1 = request.POST.get('checkbox2')
        math2 = request.POST.get('checkbox3')
        jiidan=float(Intellectual.objects.get(id=intellectuals_name).intellectual_jidina)
        if math1=="1":
            math=0.7
        else:
            math=0
        if math2=='1':
            math=math*0.5
        else:
            math=math

        book_count=math*jiidan

        username = user.username
        professor = user.professor

        rate_jidians = Work_rate_jidian.objects.get(pro_name=professor)
        Work_count.objects.create(usernum=username, count_jidians=book_count, rate_jidians=rate_jidians)
        return redirect(reverse('teacher:teachers_selcet'))


#


