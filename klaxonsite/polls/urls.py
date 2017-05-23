from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sum/(?P<a>[0-9]+)\+(?P<b>[0-9]+)/$', views.sum, name='sum'),
]
