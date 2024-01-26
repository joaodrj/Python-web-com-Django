from django.urls import path
from .views import index, contato #importando dessa aplicação index e contato do arquivo views

urlpatterns = [
    path('', index),
    path('contato', contato),
]