from django.conf.urls import  url

from .views import Show_html, Show_pie, Show_pow, Show_weblog

urlpatterns = [
    url(r'^show_html',Show_html.as_view(),name='show'),
    url(r'^show_pie',Show_pie.as_view(),name='pie'),
    url(r'^show_pow',Show_pow.as_view(),name='pow'),
    url(r'^show_weblog', Show_weblog.as_view(), name='pow'),
]
