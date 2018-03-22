
from django.conf.urls import  url

from .views import RegisterView,Excel_get,Show_html,Login

urlpatterns = [
    url(r'^register',RegisterView.as_view(),name='register'),
    url(r'^output',Excel_get.as_view(),name='output'),
    url(r'^login',Login.as_view(),name='login')
]
