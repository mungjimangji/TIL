from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('number-print/<int:num>', views.number_print, name='number'),
    path('calculate/<int:num1>/<int:num2>', views.calculate, name='calculate'),
    path('calculate-tag/', views.calculate_tag, name='calculate-tag'),
    
]