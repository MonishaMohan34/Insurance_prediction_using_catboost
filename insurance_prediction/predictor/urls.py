

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('input/', views.predict, name='predict'),  
    path('result/', views.predict, name='result'),  
]


