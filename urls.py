# djangotask2/urls.py

from django.urls import path
from .views import index, ClassTemplateView  # Импорт функции index из views

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('class/', ClassTemplateView.as_view(), name='class_template'), # Новый путь классового представления
]
