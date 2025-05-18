from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', about, name='about'),
    path('blog/list/', BlogListView.as_view(), name='blog_list'),
    path('blog/author/<str:author>/', BlogListView.as_view(), name='blog_author'),
    path('blog/tag/<str:tag>/', BlogListView.as_view(), name='blog_tag'),  # تغییر از tags به tag
    path('blog/category/<str:category>/', BlogListView.as_view(), name='blog_category'),  # تغییر از category_name به category
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]