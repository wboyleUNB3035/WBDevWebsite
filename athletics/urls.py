from django.contrib import admin
from django.urls import path, include
from athletics import views

urlpatterns = [
    path('', views.athletics, name='athletics'),
]