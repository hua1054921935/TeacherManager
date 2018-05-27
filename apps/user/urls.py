from django.conf.urls import  url

from .views import RegisterView,Excel_get,Show_html,Login,Role_select,Usermessage,Loginout,ActiveView

urlpatterns = [
    url(r'^register',RegisterView.as_view(),name='register'),
    url(r'^output',Excel_get.as_view(),name='output'),
    url(r'^$',Login.as_view(),name='login'),
    url(r'^role_select(?P<role_id>\d+)/$',Role_select.as_view(),name='role_select'),
    url(r'^selfmessage',Usermessage.as_view(),name='selfmessage'),
    url(r'^loginout', Loginout.as_view(), name='loginout'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 激活
    url(r'^Show_html',Show_html.as_view(),name='show'),
    # url(r'^output', Excel_get.as_view(), name='output'),
]
