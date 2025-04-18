from django.urls import path
from .views import *


app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
