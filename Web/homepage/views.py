from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render

pizzas_db = [
        {'id': 1, 
         'name': 'Маргарита', 
         'description': '"Маргарита" - Итальянская Классика! Сочное тесто, томатный соус, тающая моцарелла и ароматный базилик. Просто, как гениально! Состав: Тесто, томатный соус, моцарелла, базилик, оливковое масло. КБЖУ (на 100 г): 240 ккал, 11г белки, 10г жиры, 25г углеводы. Попробуйте вкус Италии!', 
         'price': 450, 
         'image_url': 'https://i.pinimg.com/736x/56/44/b3/5644b320d50cf5d58ce3a75c244c0e83.jpg', 
         'category_id': 1
        },

        {'id': 2, 
         'name': 'Пепперони', 
         'description': 'Пикантная колбаса пепперони, томатный соус и моцарелла на сочном тесте. Для любителей поострее! Состав: Тесто, томатный соус, моцарелла, пепперони, оливковое масло. КБЖУ (на 100 г): 280 ккал, 13г белки, 14г жиры, 24г углеводы. Закажите "Пепперони"!', 
         'price': 500, 
         'image_url': 'https://i.pinimg.com/736x/92/ad/03/92ad03ae1fcbc8bc94c3cc7570e0dbc6.jpg', 
         'category_id': 2
         },
    ]

categories_db = [
        {'id': 1, 'name': 'Классические'},
        {'id': 2, 'name': 'Острые'},
        {'id': 3, 'name': 'Вегетарианские'},
    ]

     
# Create your views here.
def homepage(request):
    cat_selected = request.GET.get('category_id')
    
    # Фильтрация пицц
    if cat_selected and cat_selected.isdigit() and int(cat_selected) > 0:
        # Если выбрана конкретная категория (не "Все")
        pizzas = [pizza for pizza in pizzas_db if pizza['category_id'] == int(cat_selected)]
        cat_selected = int(cat_selected)
    else:
        # Если выбрано "Все" или категория не указана
        pizzas = pizzas_db  # Показываем все пиццы
        cat_selected = 0    # 0 - это ID для "Все"

    context = {
        'headline': 'Новинка: Пицца Маргарита!',
        'description': 'Сочная пицца со свежими томатами, базиликом и сыром моцарелла',
        'cta': 'Попробуйте',
        'image_url': 'URL_ВАШЕГО_БАННЕРА',
        'title': 'Главная страница',
        'pizzas': pizzas,
        'categories': categories_db,
        'cat_selected': cat_selected
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


def category_list(request, category_id):
    """Отображает все пиццы в выбранной категории"""
    # Находим категорию
    category = next((c for c in categories_db if c['id'] == category_id), None)
    
    if not category:
        return render(request, '404.html', status=404)
    
    # Фильтруем пиццы по категории
    pizzas = [pizza for pizza in pizzas_db if pizza['category_id'] == category_id]
    
    context = {
        'category': category,
        'pizzas': pizzas,
        'categories': categories_db,
        'title': f'Пиццы категории {category["name"]}'
    }
    return render(request, 'pizza/category_list.html', context)

def pizza_detail(request, pizza_id):
   
    pizza = next((p for p in pizzas_db if p['id'] == pizza_id), None)
    
    if not pizza:
        return render(request, '404.html', status=404)
    
    context = {
        'pizza': pizza,
        'title': pizza['name'],
 
    }
    return render(request, 'pizza_detail/pizza_detail.html', context)
def current_time(request):
    return {
        'current_time': datetime.now()
    }
     



