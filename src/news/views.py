from django.shortcuts import render,get_object_or_404,redirect
from news.models import News


def news_datile(requeste,pk):
    news = News.objects.filter(pk= pk)

    return render(requeste,'front/newsdatile.html',{ 'news':news})