from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
from .mixins import BaseModelMixin


class Genre(BaseModelMixin, models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'


class Platform(BaseModelMixin, models.Model):
    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформи'


class Company(BaseModelMixin, models.Model):
    class Meta:
        verbose_name = 'Можна придбати'
        verbose_name_plural = 'Можна придбати'


class PurchaseLocation(BaseModelMixin, models.Model):
    class Meta:
        verbose_name = 'Можна придбати'
        verbose_name_plural = 'Можна придбати'


class Game(BaseModelMixin, models.Model):
    description = models.TextField('Описання', null=True)
    poster = models.ImageField('Постер', upload_to='game_poster/')
    year = models.PositiveSmallIntegerField('Рік', default=2024)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    game_file = models.FileField(upload_to='game_files/', null=True, blank=True)
    genres = models.ManyToManyField(to=Genre, verbose_name='Жанри', related_name='game_genres')
    platforms = models.ManyToManyField(to=Platform, verbose_name='Платформи', related_name='game_platforms')
    company_name = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    purchase = models.ManyToManyField(to=PurchaseLocation, verbose_name='Можна придбати', related_name='game_purchase')
    release_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField('Чорновик', default=False)

    class Meta:
        verbose_name = 'Ігра'
        verbose_name_plural = 'Ігри'


class GameScreenshot(BaseModelMixin, models.Model):
    game_name = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    image = models.ImageField('Зображеня', upload_to='game_screenshots/')
    youtube_video_url = models.URLField('Переглянути в ютубі', blank=True, null=True)

    class Meta:
        verbose_name = 'Скріншот'
        verbose_name_plural = 'Скріншоти'

