from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Blog


def index(request):
    template_name = 'news/index.html'
    context = {
        'news': Blog.objects.all()
    }

    return render(request, template_name, context)


class BlogListView(ListView):
    model = Blog
    # templateファイルの指定。　未指定の場合は {APP}/{MODEL}_{VIEW}.html
    # template_name = "news/index.html"
    context_object_name = 'blogs'
    ordering = ['-pub_date']
    paginate_by = 3


class UserBlogListView(ListView):
    model = Blog
    template_name = 'news/user_posts.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user).order_by('-pub_date')


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
