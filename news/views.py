from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog


def index(request):
    template_name = 'news/index.html'
    context = {
        'news': Blog.objects.all()
    }

    return render(request, template_name, context)


class BlogListView(ListView):
    model = Blog
    # templateファイルの指定。　未指定の場合は {PROJECT}/{MODEL}_{VIEW}.html
    # template_name = "news/index.html"
    context_object_name = "blogs"
    ordering = ['-pub_date']


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # 自分自身のみが編集可能に
    def test_func(self):
        blog = self.get_object()
        # 投稿者とログインユーザの一致
        return self.request.user == blog.author


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    # 削除後の表示ページ
    success_url = '/news'

    # 自分自身のみが編集可能に
    def test_func(self):
        blog = self.get_object()
        # 投稿者とログインユーザの一致
        return self.request.user == blog.author


def about(request):
    return render(request, 'news/about.html', {'title': 'About'})
