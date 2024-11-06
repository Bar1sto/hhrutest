from django.urls import path
from .views import get_current

urlpatterns = [
    path('get-current-usd/', get_current, name='get-current-usd'),
]