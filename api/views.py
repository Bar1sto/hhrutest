import requests, time
from django.shortcuts import render
from django.http import JsonResponse
from .models import CurrencyRequest


def fetch_exchange_rate():
    time.sleep(10)
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=97c7f1a661004288fe6b826b1ff1872c&symbols=USD,RUB&format=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and 'USD' in data['rates'] and 'RUB' in data['rates']:
            usd_to_rub = data['rates']['RUB'] / data['rates']['USD']
            return usd_to_rub
        else:
            return None
    else:
        print("Ошибка запроса:", response.status_code)
        return None


def get_current(request):
    rate = fetch_exchange_rate()

    if rate is not None:
        currency_request = CurrencyRequest.objects.create(
            currency_code='USD',
            target_currency='RUB',
            rate=rate
        )

        recent_requests = CurrencyRequest.objects.order_by('-request_date')[:10].values(
            'request_date', 'currency_code', 'target_currency', 'rate'
        )

        return JsonResponse({
            'request_date': currency_request.request_date,
            'currency_code': currency_request.currency_code,
            'target_currency': currency_request.target_currency,
            'rate': currency_request.rate,
            'recent_requests': list(recent_requests)
        })
    else:
        return JsonResponse({'error': 'Неудалось получить курс'}, status=500)
