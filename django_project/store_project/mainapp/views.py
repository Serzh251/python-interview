from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Goods


class GoodsList(ListView):
    model = Goods
    template_name = 'mainapp/good_list.html'
    extra_context = {'title': 'Главная'}