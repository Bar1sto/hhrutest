from django.contrib import admin
from django.urls import path, include
from api.urls import get_current

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls',), name='home'),
]
