from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('search', PostSearch.as_view(), name='search'),

   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', NewsEdit.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/update/', ArticleEdit.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='news_delete'),

   path('subscriptions/', subscriptions, name='subscriptions'),
]