from django.urls import path
from .views import *


app_name = 'games'
urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post_list', post_list, name='post_list'),
    path('post_detail', post_detail, name='post_detail'),
]
