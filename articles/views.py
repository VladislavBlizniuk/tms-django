from django.shortcuts import render, get_object_or_404, redirect
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {'all_articles': articles}
    return render(request, 'articles/main.html', context)


def detail(request, article_id: int):


    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def like(request):
    assert request.method == 'POST'
    article_id = request.POST['article_id']
    article = get_object_or_404(Article, id=article_id)
    article.like_count += 1
    article.save()
    return redirect('articles:detail', article.id)