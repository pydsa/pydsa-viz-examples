from django.conf.urls import include, url
from sort import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<sorting_no>\d+)/$', views.detail),
    url(r'json$', views.json_func),
]
