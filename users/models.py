from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from games.models import Game


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'


class BaseModelMixin(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)


class PurchaseHistory(BaseModelMixin, models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} - {self.purchase_date}"

    class Meta:
        verbose_name = 'Історія покупок'
        verbose_name_plural = 'Історія покупок'


class Comment(BaseModelMixin, models.Model):
    text = models.CharField(max_length=230, verbose_name='Comment')
    time_create = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('games:game_detail')

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"



