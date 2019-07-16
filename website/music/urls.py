from django.urls import path
from django.conf.urls import url
from music import views
#from . import view

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/<album_id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]