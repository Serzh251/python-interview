from django.urls import path
from .views import GoodsList

urlpatterns = [
    path('', GoodsList.as_view(), name='main'),
]
