from django.urls import converters
from django.urls import path, register_converter
from . import views
from .converters import CurrencyConverter
from .converters import FloatConverter
register_converter(CurrencyConverter, 'currency')
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', views.homepage),
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('exchange/<currency:pair>/<float:amount>/', views.exchange, name='exchange')
]