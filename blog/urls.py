from django.urls import path
from .views import *


app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('blog/list/', BlogListView.as_view(), name='blog_list'),
    path('blog/list/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
