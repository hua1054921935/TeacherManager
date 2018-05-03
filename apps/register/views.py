from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class Scinece(View):
    def get(self,request):
        return render(request,'teachering.html')
    def post(self,request):
        pass