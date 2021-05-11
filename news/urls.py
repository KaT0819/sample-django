from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]