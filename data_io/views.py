from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import pandas
import datetime
from utils.data_analys import scan_files
import numpy





class Show_html(View):
    def get(self,request):
        # 获取当前csv文件列表
        list1 = scan_files('utils/data')
        # print(list1)
        list2=[]
        list3=['2017-11-%s'%i for i in range(1,31)]

        for data in list1:

            name = data.split('/')[3]
            if name=='checking.csv':
                df = pandas.read_csv(data)
                df.drop([0],inplace=True)
                df.columns = ['id','day','qiandao','qianli']
                count=0
                for i in range(0,len(df['qiandao'])):
                    if df.iloc[i,2]=='0':
                        count += 1
                    else:
                        dt = datetime.datetime.strptime(df.iloc[i,2], "%Y-%m-%d %H:%M:%S")
                        if dt.hour>9:
                            count+=1
                list2.append(count)
        datas={'month':list3,'count':list2}
        # return render(request,'excel.html',datas)

        return render(request, 'excel.html', {'count':list2})