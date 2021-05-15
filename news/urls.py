from django.urls import path

from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = 'news'
urlpatterns = [
    path('old/', views.index, name='index-old'),
    path('', BlogListView.as_view(), name='index'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('detail/add/', BlogCreateView.as_view(), name='add'),
    path('detail/<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
    path('about', views.about, name='about'),
]
