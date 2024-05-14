from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from users.models import Comment
from .forms import CommentForm, FeedbackForm
from urllib.parse import urlencode, parse_qs, urlsplit, urlunsplit
from django.views.generic.edit import FormMixin, FormView
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseContextMixin(ListView):
    def get_context_data(self, **kwargs):
        # Отримання контексту для передачі додаткових даних в шаблон
        context = super().get_context_data(**kwargs)

        # Додаємо URL для сортування
        current_url = self.request.get_full_path()
        current_url_parts = urlsplit(current_url)
        current_query_params = parse_qs(current_url_parts.query)
        current_query_params['sort_by'] = [self.request.GET.get('sort_by', '')]
        context['sort_by_url'] = urlunsplit((current_url_parts.scheme, current_url_parts.netloc, current_url_parts.path,
                                             urlencode(current_query_params, doseq=True), current_url_parts.fragment))

        # Додаємо інші дані в контекст
        context['total_games'] = Game.objects.count()
        context['platforms'] = Platform.objects.all().order_by('name')
        context['genres'] = Genre.objects.all().order_by('name')
        context['release_date'] = Game.objects.filter().distinct('release_date').order_by('release_date')
        context['country'] = Game.objects.filter().distinct('country').order_by('country')

        return context


class GameListView(BaseContextMixin, ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/game_list.html'
    paginate_by = 15
    ordering = ['-release_date']

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', '')
        platforms = self.request.GET.getlist('platforms')
        genres = self.request.GET.getlist('genres')
        country = self.request.GET.getlist('country')
        release_date = self.request.GET.getlist('release_date')
        search_query = self.request.GET.get('search')

        # Перевірка на None та порожні рядки
        if platforms is not None or genres is not None or country is not None or release_date is not None or search_query is not None:
            queryset = Game.objects.filter(
                Q(platforms__url__in=platforms) if platforms else Q() |
                Q(genres__url__in=genres) if genres else Q() |
                Q(country__in=country) if country else Q() |
                Q(release_date__in=release_date) if release_date else Q() |
                Q(name__icontains=search_query) if search_query else Q(),
                draft=False
            ).prefetch_related('genres')

        if sort_by == 'create_date':
            queryset = queryset.order_by('create_date')
        elif sort_by == 'name':
            queryset = queryset.order_by('name')
        elif sort_by == 'price':
            queryset = queryset.order_by('price')

        return queryset.distinct()


class GenreListView(BaseContextMixin, ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/game_list.html'
    paginate_by = 15
    ordering = ['-release_date']

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', '')
        genre_slug = self.kwargs.get('genre_slug')
        genres = Genre.objects.get(url=genre_slug)
        queryset = Game.objects.filter(genres=genres, draft=False,).prefetch_related('genres')

        if sort_by == 'create_date':
            queryset = queryset.order_by('create_date')
        elif sort_by == 'name':
            queryset = queryset.order_by('name')
        elif sort_by == 'price':
            queryset = queryset.order_by('price')
        return queryset


class GameDetailView(FormMixin, DetailView):
    model = Game
    form_class = CommentForm
    context_object_name = 'game'
    slug_url_kwarg = 'game_slug'
    slug_field = 'url'

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(game=self.object)
        context['comments'] = comments
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.game = self.object
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query is not None:
            queryset = Game.objects.filter(
                Q(name__icontains=search_query) if search_query else Q()
            )
        else:
            queryset = Game.objects.all()
        return queryset.distinct()


class AboutView(TemplateView):
    template_name = 'games/about.html'


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'games/contact.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('games:contact')

    def form_valid(self, form):
        # Отримання даних з форми
        message = form.cleaned_data['message']
        sender_email = self.request.user.email if self.request.user.is_authenticated else None

        # Отправка повідомлення
        send_mail(
            'Subject of the email',
            f'Message from {sender_email}:\n\n{message}',
            sender_email,
            ['shapiktaras@gmail.com'],  # Замініть на вашу адресу електронної пошти
            fail_silently=False,
        )

        # Додавання повідомлення для користувача
        messages.success(self.request, 'Your message has been sent successfully!')

        return super().form_valid(form)

