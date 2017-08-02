from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    # url(r'^pop/$', views.search,name='popular'),
    # url(r'^search/$', views.search,name='search'),
    url(r'^video/(?P<video_id>[a-zA-Z0-9-]*)$', views.watch,name='watch'),
    url(r'^download/(?P<video_id>[a-zA-Z0-9-]*)$', views.download,name='download'),
]
