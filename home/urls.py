from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projectOne', views.projectOne, name='projectOne'),
    path('projectTwo', views.projectTwo, name='projectTwo'),
    path('projectThree', views.projectThree, name='projectThree'),
    path('projectFour', views.projectFour, name='projectFour'),
    path('projectFive', views.projectFive, name='projectFive'),
    path('projectSix', views.projectSix, name='projectSix'),
]
