from unicodedata import name
from django.urls import path
from Blog import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
]
