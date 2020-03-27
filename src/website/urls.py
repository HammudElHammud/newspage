"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from  django.conf import settings
from django.conf.urls.static import static
from main import models,views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('main.urls')),
    url(r'^home/$',views.home,name='home'),
    url(r'^about/$',views.about,name='about'),
    url(r'^panel/$',views.panel,name='panel '),
    url(r'^panel/category$',views.CategoryList,name='category '),
    url(r'^panel/subcategory$',views.subCategoryList,name='subcategory '),
    url(r'^panel/addCategory/$',views.addCategory,name='addCategory'),
    url(r'^panel/addSubCategory/$',views.addSubCategory,name='addSubCategory'),
    url(r'^panel/newAdd/$',views.newAdd,name='newAdd'),
    url(r'^panel/nowNews/$',views.nowNewsDtaile,name='nowNews '),
    url(r'^/message/$',views.adminMessage,name='message'),
    url(r'^login/$',views.login ,name='login'),
    url(r'^register/$',views.register ,name='register'),
    url(r'^contant/$',views.contant ,name='contant'),
    url(r'^logout/$',views.logout ,name='logout'),
    url(r'^settingPage/$',views.settingPage ,name='settingPage'),
    url(r'^news/(?P<pk>\d+)/$', views.news_datile, name='news_datile'),
    url(r'^contentDelete/(?P<pk>\d+)/$', views.contentDelete, name='contentDelete'),
    url(r'^panel/newDel/(?P<pk>\d+)/$', views.newsDelete, name='newsDelete'),
    url(r'^panel/news_edit/(?P<pk>\d+)/$',views.news_edit, name='news_edit'),
    url(r'^panel/categoryDel/(?P<pk>\d+)/$', views.categoryDelete, name='categoryDelete'),
    url(r'^panel/subcategoryDel/(?P<pk>\d+)/$', views.subcategoryDelete, name='subcategoryDelete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
