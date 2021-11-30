from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Goods, Category


class GoodsList(ListView):
    model = Goods
    template_name = 'mainapp/good_list.html'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *args, **kwargs):
        contex = super().get_context_data(*args, **kwargs)
        # contex['site'] = self.request.site
        return contex


class Category(ListView):
    model = Goods
    template_name = 'mainapp/good_list.html'
    extra_context = {'title': 'Главная'}

    def get_queryset(self):
        if self.kwargs["pk"] == 0:
            goods = Goods.on_site.prefetch_related('category').all()
        else:
            goods = Goods.on_site.prefetch_related('category').filter(category=self.kwargs["pk"])
        return goods

    def get_context_data(self, *args, **kwargs):
        contex = super().get_context_data(*args, **kwargs)
        contex['site'] = self.request.site
        return contex
