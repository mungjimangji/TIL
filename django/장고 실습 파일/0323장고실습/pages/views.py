from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def number_print(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'pages/number_print.html', context)

def calculate(request, num1, num2):
    add = num1 + num2
    minus = num1 - num2
    multi = num1 * num2
    quo = num1 // num2
    context = {
        'add' : add,
        'minus' : minus,
        'multi' : multi,
        'quo' : quo,
        
    }
    return render(request, 'pages/calculate.html', context)

def calculate_tag(request):
    return render(request, 'pages/calculate_tag.html')
    
    

