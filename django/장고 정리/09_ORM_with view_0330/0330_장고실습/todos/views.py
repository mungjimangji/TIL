from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render (request, 'todos/index.html', context)

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }

    return render(request, 'todos/detail.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    completed = request.POST.get('completed')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    print(request.POST)
   

    todo = Todo(title=title, content=content, priority=priority, deadline=deadline, completed=completed)
    todo.save()
    
    return redirect('todos:detail', todo.pk)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.delete()
    return redirect('todos:index')

def edit(request, pk):
    todo = Todo.objects.get(pk=pk)

    context = {
        'todo' : todo,
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')

    todo.save()
    return redirect('todos:detail', todo.pk)

def complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    print(type(request.POST.get('completed')))
    if request.POST.get('completed') == 'True':
        print(1)
        todo.completed = False
        todo.save()
    elif request.POST.get('completed') == 'False':
        print(2)
        todo.completed = True
        todo.save()

    return redirect('todos:index')