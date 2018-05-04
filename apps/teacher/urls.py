
from django.conf.urls import  url

from .views import Teachers_work

urlpatterns = [
    url(r'^teachers_work',Teachers_work.as_view(),name='teachers_work'),
    # url(r'^output',Excel_get.as_view(),name='output'),
    # url(r'^login',Login.as_view(),name='login'),
    # url(r'^role_select',Role_select.as_view(),name='role_select'),
    # url(r'^selfmessage',Usermessage.as_view(),name='selfmessage')

]
