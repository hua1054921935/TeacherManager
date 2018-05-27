from openpyxl import load_workbook
import pandas
from apps.user.models import User,Role
from apps.teacher.models import Work_count,Work_rate_jidian

def read_xls(self,request,obj, change):
    print(obj.file)
    df=pandas.read_excel(obj.file)
    print(df)
    # df.drop([0],inplace=True)
    # df.columns = ['username','sex','age']
    for i in range(0,len(df['学工号'])):
        username=df.iloc[i,0]
        email=df.iloc[i,1]
        professor=df.iloc[i,2]
        jidian=df.iloc[i,3]
        password=123456
        role_id=df.iloc[i,4]
        #导入用户信息
        role = Role.objects.get(id=role_id)
        user = User()
        user.username = username
        user.role = role
        user.professor = professor
        user.email = email
        user.set_password(password)
        user.is_active = 1
        user.save()
        #导入绩点信息
        rate_jidians = Work_rate_jidian.objects.get(pro_name=professor)
        id=User.objects.get(username=username).id
        Work_count.objects.create(usernum=id, count_jidians=jidian, rate_jidians=rate_jidians)
    return 'success'

