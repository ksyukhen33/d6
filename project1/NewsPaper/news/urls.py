from django.urls import path
from .views import (PostsList, PostDetail, PostsCreate, PostsUpdate, PostsDelete, PostsSearch, ArticleCreate,
                    ArticleUpdate, ArticleDelete, ArticleList, subscriptions)


urlpatterns = [
    path('posts/', PostsList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', PostsCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostsUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', PostsDelete.as_view(), name='posts_delete'),
    path('search/', PostsSearch.as_view(), name='posts_search'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('article/', ArticleList.as_view(), name='article_list'),
    path('subscriptions/', subscriptions, name='subscriptions'),

]

