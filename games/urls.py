from django.urls import path
from .views import *


app_name = 'games'
urlpatterns = [
    path('', GameListView.as_view(), name='game_list'),

    path('<slug:game_slug>/', GameDetailView.as_view(), name='game_detail'),


    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
