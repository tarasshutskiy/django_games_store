from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


class BaseModelMixin(models.Model):
    name = models.CharField(max_length=255)
    url = models.SlugField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(unidecode(self.name))
            counter = 1
            while self.__class__.objects.filter(url=self.url).exclude(pk=self.pk).exists():
                self.url = f"{slugify(unidecode(self.name))}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(f'games:{self._meta.model_name}', kwargs={f'{self._meta.model_name}_slug': self.url})


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
        verbose_name = 'Компанія'
        verbose_name_plural = 'Компанія'


class Game(BaseModelMixin, models.Model):
    description = models.TextField('Описання', null=True)
    poster = models.ImageField('Постер', upload_to='game_poster/')
    steam = models.URLField('Steam', blank=True, null=True)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    game_file = models.FileField('Файли з грою', upload_to='game_files/', null=True, blank=True)
    country = models.CharField('Країна', max_length=120, null=True)
    genres = models.ManyToManyField(to=Genre, verbose_name='Жанри', related_name='game_genres')
    platforms = models.ManyToManyField(to=Platform, verbose_name='Платформи', related_name='game_platforms')
    company_name = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    release_date = models.DateField('Рік', default=2024)
    create_date = models.DateTimeField('Дата створення поста', auto_now_add=True)
    youtube_video_url = models.URLField('Переглянути в ютубі', blank=True, null=True)
    draft = models.BooleanField('Чорновик', default=False)

    class Meta:
        verbose_name = 'Ігра'
        verbose_name_plural = 'Ігри'

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


class GameScreenshot(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    game_name = models.ForeignKey(to=Game, on_delete=models.CASCADE)
    image = models.ImageField('Зображеня', upload_to='game_screenshots/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скріншот'
        verbose_name_plural = 'Скріншоти'


#     def get_model_name(self):
#         return self._meta.model_name
#
# instance = GameScreenshot()
# model_name = instance.get_model_name()
# print(model_name)