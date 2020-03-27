from django.contrib import admin
from django.conf.urls import url
from . import views



urlpatterns = {

    url(r'^news/(?<pk>\d+)/$', views.news_datile, name='news_datile'),
}