from django.shortcuts import render
from django.views.generic import View
from .models import Teacher_work
# Create your views here.
# 教师业绩量化
class Teachers_work(View):
    def get(self,request):
        data_list=Teacher_work.objects.all()
        return render(request,'teachering.html',{'data_list':data_list})
    def post(self,request):
        pass