from django.conf.urls import url

from .views import Scinece, ShowData

urlpatterns = [
    url(r'^show_scinece', Scinece.as_view(), name='show_scinece'),
    url(r'^showdata', ShowData.as_view(), name='showdata'),

]
