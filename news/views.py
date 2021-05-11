from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Blog


def index(request):
    template_name = 'news/index.html'
    context = {
        'news': Blog.objects.all()
    }

    return render(request, template_name, context)


def about(request):
    return render(request, 'news/about.html', {'title': 'About'})
