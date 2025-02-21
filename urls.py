from django.urls import path
from .views import home, products, basket

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('basket/', basket, name='basket'),
]