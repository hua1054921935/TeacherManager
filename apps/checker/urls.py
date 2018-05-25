from django.conf.urls import url

from .views import Scinece, ShowData, Cherker_index

urlpatterns = [
    url(r'^show_scinece', Scinece.as_view(), name='show_scinece'),
    url(r'^showdata', ShowData.as_view(), name='showdata'),
    url(r'^checker_index,', Cherker_index.as_view(), name='checker_index')

]
