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
