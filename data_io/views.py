import datetime

import pandas
from django.shortcuts import render
from django.views.generic import View

from utils.data_analys import scan_files


class Show_html(View):
    def get(self,request):
        # 获取当前csv文件列表
        list1 = scan_files('utils/data')
        # print(list1)
        list2=[]
        list3 = ["2017-11-%s" % i for i in range(1, 31)]

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
        list2.reverse()
        datas={'month':list3,'count':list2}



        return render(request, 'excel.html',datas)


class Show_pie(View):
    def get(self,request):
        list1 = scan_files('utils/data')
        list1.sort()
        list2 = []
        list3 = ["2017-11-%s" % i for i in range(1, 31)]
        flag = 1
        for data in list1:
            dict2 = {}
            count=0

            name = data.split('/')[3]
            if name=='login.csv':
                df = pandas.read_csv(data)
                df.drop([0], inplace=True)
                df.columns=['proto','dip','dport','sip','sport','state','time','user']
                counts = df['time'].value_counts()
                print(counts)
                for i in range(0,len(df['state'])):
                    if df.iloc[i,5]=='error':
                        count+=1
                dict2['flag'] = '2017-11-' + str(flag)
                # dict2['flag'] =flag
                dict2['count']=count
                list2.append(dict2)
                flag+=1

        return render(request, 'login_count.html', {'list2': list2, 'list3': list3})

class Show_pow(View):
    def get(self,request):
        list1 = scan_files('utils/data')
        list1.sort()
        for data in list1:
            name = data.split('/')[3]
            if name == 'email.csv':
                df = pandas.read_csv(data, encoding='ISO-8859-1')
                df.drop([0], inplace=True)
                df.columns =['time','proto','sip','sport','dip','dport','from','to','subject']
                counts = df['from'].value_counts()

        return render(request, 'login_count.html')


class Show_weblog(View):
    def get(self, request):
        list1 = scan_files('utils/data')
        list1.sort()
        for data in list1:
            name = data.split('/')[3]
            if name == 'weblog.csv':
                df = pandas.read_csv(data, encoding='ISO-8859-1')
                df.drop([0], inplace=True)
                df.columns = ['time', 'sip', 'sport', 'dip', 'dport', 'host']
                counts = df['host'].value_counts()
                print(counts)
        return render(request, 'login_count.html')


class Show_login(View):
    def get(self, request):
        list1 = scan_files('utils/data')
        list1.sort()
        for data in list1:
            name = data.split('/')[3]
            if name == 'weblog.csv':
                df = pandas.read_csv(data, encoding='ISO-8859-1')
                df.drop([0], inplace=True)
                df.columns = ['time', 'sip', 'sport', 'dip', 'dport', 'host']
                counts = df['host'].value_counts()
                print(counts)
        return render(request,'login_count.html')