
from django.conf.urls import  url

from .views import Teacher_selcet,Teachers_book,Teachers_pingtai,Teachers_yan

urlpatterns = [
    url(r'^teachers_work',Teachers_yan.as_view(),name='teachers_work'),
    url(r'^teachers_selcet',Teacher_selcet.as_view(),name='teachers_selcet'),
    url(r'^teachers_pingtai',Teachers_pingtai.as_view(),name='teachers_pingtai'),
    url(r'^teachers_book',Teachers_book.as_view(),name='teachers_book'),

    # url(r'^output',Excel_get.as_view(),name='output'),
    # url(r'^login',Login.as_view(),name='login'),
    # url(r'^role_select',Role_select.as_view(),name='role_select'),
    # url(r'^selfmessage',Usermessage.as_view(),name='selfmessage')

]
