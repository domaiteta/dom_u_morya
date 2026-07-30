from django.db import models
from django.urls import reverse


class House(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(verbose_name="Фотография", upload_to="houses/photos", blank=True, default="")

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

        ordering = ['price']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('house_detail', args=(self.pk,))
