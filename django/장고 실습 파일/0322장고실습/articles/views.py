from django.shortcuts import render
from random import *

# Create your views here.
def today_dinner(request):
    foods = ['치킨', '삼겹살', '자장면',]
    context = {
        'foods' : foods,
    }
    return render(request, 'articles/today-dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data' : data,
    }
    return render(request, 'articles/catch.html', context)

def lotto_create(request):
    return render(request, 'articles/lotto_create.html')

def lotto(request):
    numbers = [num for num in range(1,46)]
    lotto_numbers = []
    data = int(request.GET.get('message'))
    for _ in range(data):
        lotto_numbers.append(sample(numbers, 6))
   
    context = {
        'data' : data,
        'lotto_numbers' : lotto_numbers,
    }
    return render(request, 'articles/lotto.html', context)