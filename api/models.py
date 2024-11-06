from django.db import models


class CurrencyRequest(models.Model):
    request_date = models.DateTimeField(auto_now_add=True)
    currency_code = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
