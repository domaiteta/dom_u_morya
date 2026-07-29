from django.db import models

class House(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
