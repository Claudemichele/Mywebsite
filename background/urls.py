from . import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.postList, name='postList'),
    url(r'^about', views.about, name='about'),
    url(r'^$', views.index, name='index'),


]