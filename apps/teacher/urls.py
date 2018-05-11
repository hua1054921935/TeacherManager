
from django.conf.urls import  url

from .views import Teacher_selcet,Teachers_book,Teachers_pingtai,Teachers_yan,Teachers_science,Teachers_thesis,Teachers_chanquan,Teachers_zzyj,Teachers_proj,Teachers_reward,Teachers_scpitai,Teachers_chuban,Teachers_zhanlan,Teachers_huojiang,Teachers_xuewei

urlpatterns = [
    url(r'^teachers_work',Teachers_yan.as_view(),name='teachers_work'),
    url(r'^teachers_selcet',Teacher_selcet.as_view(),name='teachers_selcet'),
    url(r'^teachers_pingtai',Teachers_pingtai.as_view(),name='teachers_pingtai'),
    url(r'^teachers_book',Teachers_book.as_view(),name='teachers_book'),
    url(r'^teachers_science',Teachers_science.as_view(),name='teachers_science'),
    url(r'^teachers_thesis',Teachers_thesis.as_view(),name='teachers_thesis'),
    url(r'^teachers_chanquan',Teachers_chanquan.as_view(),name='teachers_chanquan'),
    url(r'^teachers_zzyj',Teachers_zzyj.as_view(),name='teachers_zzyj'),
    url(r'^teachers_proj',Teachers_proj.as_view(),name='teachers_proj'),
    url(r'^teachers_reward',Teachers_reward.as_view(),name='teachers_reward'),
    url(r'^teachers_scpitai',Teachers_scpitai.as_view(),name='teachers_scpitai'),
url(r'^teachers_chuban',Teachers_chuban.as_view(),name='teachers_chuban'),
url(r'^teachers_huojiang',Teachers_huojiang.as_view(),name='teachers_huojiang'),
url(r'^teachers_zhanlan',Teachers_zhanlan.as_view(),name='teachers_zhanlan'),
url(r'^teachers_xuewei',Teachers_xuewei.as_view(),name='teachers_xuewei'),


    # url(r'^output',Excel_get.as_view(),name='output'),
    # url(r'^login',Login.as_view(),name='login'),
    # url(r'^role_select',Role_select.as_view(),name='role_select'),
    # url(r'^selfmessage',Usermessage.as_view(),name='selfmessage')

]
