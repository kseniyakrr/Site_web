from unicodedata import category
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Pizza, Category, TagPost


     
def homepage(request):
    # Получаем все пиццы с оптимизацией запросов
    
    pizzas = Pizza.objects.filter(is_available=True).select_related("category")
    
    context = {
        'title': 'Главная страница',
        'pizzas': pizzas,
        'categories': Category.objects.all(),
        'pizzas': Pizza.objects.all(),
        'cat_selected': 0,  # Не используем фильтрацию на сервере
    }
    return render(request, 'homepage/homepage/homepage.html', context)




def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')

def exchange(request, pair, amount):
    """Пример простого конвертера валют"""
    rates = {
        # Прямые курсы
        'USD-RUB': 90.50,
        'EUR-USD': 1.07,
        'EUR-RUB': 96.80,
        
        # Обратные курсы (1 / прямой курс)
        'RUB-USD': round(1 / 90.50),
        'USD-EUR': round(1 / 1.07),
        'RUB-EUR': round(1 / 96.80),
        
        # Само-конвертации (курс 1:1)
        'USD-USD': 1.0,
        'EUR-EUR': 1.0,
        'RUB-RUB': 1.0

    }
    try:
        # Обработка входных данных
       
        if amount <= 0:
            raise ValueError
        pair_upper = pair.upper()
        if pair_upper not in rates:
            raise KeyError
            
        # Вычисление результата
        converted = round(amount * rates[pair_upper], 2)
        from_cur = pair_upper[:3]
        to_cur = pair_upper[4:]
        rate = rates[pair_upper]
        
        # Форматирование заголовка
        result_html = f"""
           <h1>Результат конвертации</h1>
           <p><strong>Дата:</strong> {datetime.now().strftime('%d.%m.%Y %H:%M')}</p>
           <p><strong>Сумма:</strong> {amount} {from_cur}</p>
           <p><strong>Курс:</strong> 1 {from_cur} = {rate} {to_cur}</p>
           <h2>Итого: {converted} {to_cur}</h2>
           """
        return HttpResponse(result_html)

    except ValueError:
        return HttpResponse("ОШИБКА: Некорректная сумма", status=400)
    except KeyError:
        return HttpResponse("ОШИБКА: Неподдерживаемая валютная пара", status=400)
    



def menu(request, category_id=0):
    """Отображение пицц по выбранной категории."""
    pizzas = [pizza for pizza in pizzas_db if pizza['category_id'] == category_id or category_id == 0] # List comprehension.

    context = {
        'headline': 'Наше меню',
        'description': 'Выбирайте пиццу на свой вкус!',
        'cta': 'Подробнее',
        'image_url': '/static/images/menu.jpg',
        'title': 'Категории пицц',
        'pizzas': pizzas,
        'categories': categories_db,
        'cat_selected': category_id,
    }
    return render(request, 'menu/menu.html', context)


def category_list(request, category_slug):
    """Отображает все пиццы в выбранной категории"""
    category = get_object_or_404(Category, slug=category_slug)
    
    # Получаем доступные пиццы этой категории
    pizzas = Pizza.available.filter(category__slug=category_slug)

    context = {
        'category': category,
        'pizzas': Pizza.objects.all(),
        'categories': Category.objects.all(),
        'title': f'Пиццы категории {category.name}',
        'cat_selected': category.slug  # Передаем slug категории
    }

    return render(request, 'homepage/category_list.html', context)

def pizza_detail(request, pizza_slug):
    pizza = get_object_or_404(Pizza, slug=pizza_slug)  # Исправлено 'slug-pizza_slug' на 'slug=pizza_slug'
    return render(request, 'pizza_detail/pizza_detail.html', {'pizza': pizza})

def current_time(request):
    return {
        'current_time': datetime.now()
    }
     

def show_tag(request, tag_slug=None):
    tag = None
    pizzas = Pizza.objects.all()
    
    if tag_slug:
        tag = get_object_or_404(TagPost, slug=tag_slug)
        pizzas = pizzas.filter(tags__in=[tag])
    
    return render(request, 'homepage/homepage.html', {
        'pizzas': pizzas,
        'tag': tag
    })

