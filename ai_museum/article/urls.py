from django.contrib import admin
from django.urls import path, include
from article import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<article_id>/', views.ArticleDetailView.as_view()),
    path('<article_id>/', views.ArticleView.as_view()),
    path('comment/', views.CommentView.as_view()),
    path('<article_id>/comment/', views.CommentView.as_view()),
    path('<article_id>/like/', views.LikeView.as_view()),
]