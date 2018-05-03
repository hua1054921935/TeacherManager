
from django.conf.urls import  url

# from .views import RegisterView,Excel_get,Show_html,Login,Showinfo
from .views import Scinece

urlpatterns = [
    # url(r'^register',RegisterView.as_view(),name='register'),
    # url(r'^output',Excel_get.as_view(),name='output'),
    # url(r'^login',Login.as_view(),name='login'),
    # url(r'^show_info',Showinfo.as_view(),name='show_info')
    url(r'^showteachering',Scinece.as_view(),name='scence')
]
