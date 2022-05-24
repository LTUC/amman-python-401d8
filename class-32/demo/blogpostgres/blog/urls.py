from django.urls import path
from blog.api.viewsets import (
                            ArticlesDetailView, 
                            ArticlesListView
                        )

urlpatterns = [
    path('articles-list', ArticlesListView.as_view(), name = 'articles_list'),
    path('article-detail/<int:pk>', ArticlesDetailView.as_view(), name = 'article_detail'),

]