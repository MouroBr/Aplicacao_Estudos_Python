"""
    AQUI FICAM AS ROTAS QUE CHAMAM O BANCO 
"""

from django.contrib import admin
from django.urls import path
from hotel.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
