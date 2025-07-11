from django.urls import path 
from . import views

urlpatternd = [
    path('playground/hello', views.say_hello)
]