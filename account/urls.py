from django.urls import path
from .views import *
urlpatterns = [
    path('test/login/', login, name='test'),
    path('test/register/', register, name='test'),
]