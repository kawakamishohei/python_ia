from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/list/', views.ArticleListView.as_view(), name='article_list'),
    path('article/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('tag/list/', views.TagListView.as_view(), name='tag_list'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article_update/<int:pk>/', views.ArticleUpdate.as_view(), name='article_update'),
    path('article_delete/<int:pk>/',views.ArticleDelete.as_view(), name='article_delete'),
    path('comment/create/<int:pk>',views.CommentCreateView.as_view(), name='comment_create'),
]
