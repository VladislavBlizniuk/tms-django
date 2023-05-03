from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Article

# Create your views here.


def index(request: HttpRequest):
    articles = Article.objects.all
    context = {'articles_list': articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def like(request, article_id: int):
    assert request.method == 'POST'
    article_id = request.POST['article_id']
    article = get_object_or_404(Article, id=article_id)
    like_session = request.session.get("like_object", [])
    if article_id in like_session:
        like_session.remove(article_id)
        article.like_count -= 1
    else:
        like_session.append(article_id)
        article.like_count += 1
    request.session['like_object'] = like_session
    article.save()
    return redirect('articles:detail', article.id)