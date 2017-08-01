from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url(r'^pop/$', views.search,name='popular'),
    # url(r'^search/$', views.search,name='search'),
    url(r'^video/(?P<video_id>[a-zA-Z0-9-]*)$', views.watch,name='watch'),
]
