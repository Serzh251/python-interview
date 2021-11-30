from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(max_length=20, db_index=True, verbose_name='Название категории')
    is_active = models.BooleanField('активность', default=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return f'{self.name}'


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
    category = models.ManyToManyField(Category, verbose_name='Категория товара', related_name='category')
    site = models.ManyToManyField(Site)
    objects = models.Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return f'Товар {self.name} поставщик {self.provider}'

