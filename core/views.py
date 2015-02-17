from django.shortcuts import render

from core.models import Article

def main(request):
    return render(request, "main.html", {
        'articles': Article.objects.all(),
        'request': request,
        'site': 'main',
    })

def article(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    return render(request, "article.html", {
        'article': article,
        'articles': Article.objects.all(),
        'request': request,
        'site': 'article',
    })
