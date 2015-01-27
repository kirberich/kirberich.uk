from django.shortcuts import render

from core.models import Article

# Create your views here.
def main(request):
    return render(request, "main.html", {'articles':Article.objects.all()})
