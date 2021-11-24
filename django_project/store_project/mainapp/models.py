from django.db import models


class Goods(models.Model):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    UNIT_CHOICES = [
        ('rub', 'Рубли'),
        ('usd', 'Доллары'),
        ('euro', 'Евро')
    ]
    DEFAULT_UNIT = 'rub'

    name = models.CharField(max_length=300, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    unit = models.CharField(verbose_name='Единица измерения валюты', max_length=6,
                            choices=UNIT_CHOICES, default=DEFAULT_UNIT)
    provider = models.CharField(max_length=300, verbose_name='Имя поставщика')

    def __str__(self):
        return f'Товар {self.name} поставщик {self.provider} '