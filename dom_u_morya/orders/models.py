from django.db import models

class Order(models.Model):
    house = models.ForeignKey(to='houses.House', on_delete=models.CASCADE, verbose_name='Дом')
    name = models.CharField(verbose_name='Имя', max_length=50)
    phone = models.CharField(verbose_name='Телефон', max_length=50)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
