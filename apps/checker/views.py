from django.shortcuts import render
from django.views.generic import View

from apps.teacher.models import Work_count
from apps.user.models import User


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
            username = data.username
            list1.append(int(username))

            teacher_count = Work_count.objects.filter(usernum=username)
            data = 0
            for count in teacher_count:
                data = data + count.count_jidians
            list2.append(data)
        dict1['username'] = list1
        dict1['jiidan'] = list2
        print(dict1)
        return render(request, 'checker_show.html', dict1)
    def post(self):
        pass


class Cherker_index(View):
    def get(self, request):
        return render(request, 'checker_index.html')
