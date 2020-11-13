from django.urls import path, include
from apps.adopcion.views import index


urlpatterns = [
    path('index', index),
]