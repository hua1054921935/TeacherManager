
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader
import os
from celery import Celery
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TeacherManager.settings")
django.setup()


#建立celery类对像
app=Celery('celery_tasks.tasks',broker='redis://127.0.0.1:6379/11')

@app.task
def send_mail_register(email,username,token):
    '''发送激活邮件'''
    # 组织邮件内容
    subject = '教师业绩量化'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [email]
    html_message = """
                        <h1>%s, 欢迎您成为教师业绩量化注册会员</h1>
                        请点击以下链接激活您的账户<br/>
                        <a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>
                    """ % (username, token, token)

    # 发送激活邮件
    # send_mail(subject=邮件标题, message=邮件正文,from_email=发件人, recipient_list=收件人列表)
    send_mail(subject, message, sender, receiver, html_message=html_message)




