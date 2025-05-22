from django.urls import converters
from django.urls import path, register_converter
from . import views
from .converters import CurrencyConverter
from .converters import FloatConverter
register_converter(CurrencyConverter, 'currency')
register_converter(FloatConverter, 'float')
from .views import PizzaCategory, addpage


urlpatterns = [
    path('', views.PizzaHome.as_view(), name='homepage'),
    path('pizza/<slug:pizza_slug>/', views.ShowPost.as_view(), name='pizza_detail'),
    path('menu/', views.menu, name='menu'),  
    path('category/<slug:cat_slug>/', views.PizzaCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('about/', views.about, name='about'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<int:pk>/', views.DeletePizza.as_view(), name='delete_pizza'),
]