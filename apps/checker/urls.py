from django.conf.urls import url

from .views import Scinece, ShowData, Cherker_index,Checker_message,Checker_select_all,Checker_shehe,Excel_get

urlpatterns = [
    url(r'^show_scinece', Scinece.as_view(), name='show_scinece'),
    url(r'^showdata', ShowData.as_view(), name='showdata'),
    url(r'^checker_index', Cherker_index.as_view(), name='checker_index'),
    url(r'^checker_message', Checker_message.as_view(), name='checker_message'),
    url(r'^checker_select_all', Checker_select_all.as_view(), name='checker_select_all'),
    url(r'^checker_shehe(.*)/$', Checker_shehe.as_view(), name='checker_shehe'),
    url(r'^Excel_get', Excel_get.as_view(), name='Excel_get'),


]
