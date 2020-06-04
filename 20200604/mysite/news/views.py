from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__month=month, pub_date__year=year)
    context = {'month': month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context)


def article_detail(request,year,month,pk):
    article = Article.objects.get(pk=pk)
    context = {'id': pk, 'article': article}
    return render(request, 'news/article_detail.html', context)