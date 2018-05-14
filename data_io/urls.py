
from django.conf.urls import  url

from .views import Show_html

urlpatterns = [
    url(r'^show_html',Show_html.as_view(),name='show'),

]
