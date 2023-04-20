from django.urls import path, re_path
from .views import (
    news_list,
    news_detail,
    news_create,
    news_edit,
    news_delete
)

from django.conf.urls import handler404
handler404 = 'NewsApp.views.handler404'

urlpatterns = [
    path('', news_list, name='news-home'),
    path('news/<int:pk>/', news_detail, name='news-detail'),
    path('news/createnew/', news_create, name='news-create'),
    path('news/<int:pk>/edit/', news_edit, name='news-update'),
    path('news/<int:pk>/delete/', news_delete, name='news-delete'),
]