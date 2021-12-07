from django.urls import path
from .views import GoodsList, Category

urlpatterns = [
    path('', GoodsList.as_view(), name='main'),
    path('category/<int:pk>/', Category.as_view(), name='category'),
]
