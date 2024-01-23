from django.urls import path
from .views import *

app_name = 'games'
urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),


    path('<slug:game_slug>/', GameDetailView.as_view(), name='game_detail'),
    path('genre/<slug:genre_slug>/', GenreListView.as_view(), name='genre_list'),
]
