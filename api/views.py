from django.shortcuts import render
from django.http import JsonResponse
from .models import CurrencyRequest

def get_current(request):
    model = CurrencyRequest.objects.all()
    return JsonResponse({
        'request_date': 'request_date',
        'currency_code': 'currency_code',
        'target_currency': 'target_currency',
        'rate': 'rate',
    })
