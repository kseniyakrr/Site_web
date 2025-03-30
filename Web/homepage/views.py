from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    return HttpResponse('<h1>Добро пожаловать на главную страницу!</h1>')

def pizza_detail(request, pizza_id):
 if pizza_id > 10:
     raise Http404()
 
 if request.GET:
     print(request.GET)

 return HttpResponse(f"<h1>Пицца</h1><p>ID: {pizza_id}</p>")

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
    


