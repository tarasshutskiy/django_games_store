from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .forms import *


class GameListView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/game_list.html'

    def get_queryset(self):
        platforms = self.request.GET.getlist('platforms')
        genres = self.request.GET.getlist('genres')
        country = self.request.GET.getlist('country')
        search_query = self.request.GET.get('search')

        # Перевірка на None та порожні рядки
        if platforms is not None or genres is not None or country is not None or search_query is not None:
            queryset = Game.objects.filter(
                Q(platforms__url__in=platforms) if platforms else Q() |
                Q(genres__url__in=genres) if genres else Q() |
                Q(country__in=country) if country else Q() |
                Q(name__icontains=search_query) if search_query else Q()
            )
        else:
            queryset = Game.objects.all()

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        # Отримання контексту для передачі додаткових даних в шаблон
        context = super().get_context_data(**kwargs)
        context['total_games'] = Game.objects.count()
        context['platforms'] = Platform.objects.all()
        context['genres'] = Genre.objects.all()
        context['country'] = Game.objects.filter().distinct('country')

        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'create_date':
            context['games'] = context['games'].order_by('-create_date')
        elif sort_by == 'name':
            context['games'] = context['games'].order_by('name')

        return context


class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    slug_url_kwarg = 'game_slug'
    slug_field = 'url'


class AboutView(TemplateView):
    template_name = 'games/about.html'


class ContactView(TemplateView):
    template_name = 'games/contact.html'
