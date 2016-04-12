from django.conf.urls import patterns, url
from sort import views
from sort.models import Sorting


urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^(?P<sorting_no>\d+)/$', views.detail, name='detail'),
    url(r'^json$', views.json_func, name='json'),
)
