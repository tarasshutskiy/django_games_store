from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

from urllib.parse import urlencode, parse_qs, urlsplit, urlunsplit


class GameListView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/game_list.html'
    filter_params = ['platforms', 'genres', 'country', 'search']

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', '')
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

        if sort_by == 'create_date':
            queryset = queryset .order_by('create_date')
        elif sort_by == 'name':
            queryset = queryset .order_by('name')

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        # Отримання контексту для передачі додаткових даних в шаблон
        context = super().get_context_data(**kwargs)

        # Додаємо приховані поля для параметрів фільтрації та сортування
        for filter_param in self.filter_params:
            context[f'{filter_param}_url'] = ', '.join(self.request.GET.getlist(filter_param)) if filter_param in [
                'platforms', 'genres'] else self.request.GET.getlist(filter_param)

        # Додаємо URL для сортування
        current_url = self.request.get_full_path()
        current_url_parts = urlsplit(current_url)
        current_query_params = parse_qs(current_url_parts.query)
        current_query_params['sort_by'] = [self.request.GET.get('sort_by', '')]
        context['sort_by_url'] = urlunsplit((current_url_parts.scheme, current_url_parts.netloc, current_url_parts.path,
                                             urlencode(current_query_params, doseq=True), current_url_parts.fragment))

        # Додаємо інші дані в контекст
        context['total_games'] = Game.objects.count()
        context['platforms'] = Platform.objects.all()
        context['genres'] = Genre.objects.all()
        context['country'] = Game.objects.filter().distinct('country')

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
