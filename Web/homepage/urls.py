from django.urls import converters
from django.urls import path, register_converter
from . import views
from .converters import CurrencyConverter
from .converters import FloatConverter
register_converter(CurrencyConverter, 'currency')
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pizza/<slug:pizza_slug>/', views.pizza_detail, name='pizza_detail'),
    path('menu/', views.menu, name='menu'),  
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('tag/<slug:tag_slug>/', views.show_tag, name='tag'),
    
]