from django.db import models

class House(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

        ordering = ['price']

    def __str__(self):
        return f"{self.name}"
