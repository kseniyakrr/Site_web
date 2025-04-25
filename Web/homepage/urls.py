from django.urls import converters
from django.urls import path, register_converter
from . import views
from .converters import CurrencyConverter
from .converters import FloatConverter
register_converter(CurrencyConverter, 'currency')
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pizza/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('menu/', views.menu, name='menu'),  
    path('category/<int:category_id>/', views.category_list, name='category_list'),
    
]