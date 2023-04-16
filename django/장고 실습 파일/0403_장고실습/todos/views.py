# Create your views here.
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }

    return render(request, 'todos/index.html', context)

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }

    return render(request, 'todos/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:  
      form = TodoForm()
    context = {
        'form' : form,
    }
    return render(request, 'todos/new.html', context)
        

def delete(request, pk):
    # 삭제할 데이터 조회
    todo = Todo.objects.get(pk=pk)

    # 조회한 데이터 삭제(DELETE)
    todo.delete()

    # 전체 조회 페이지 이동
    return redirect('todos:index')

def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
        
    else:  
      form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form' : form,
    }
    return render(request, 'todos/edit.html', context)


# def edit(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     form = TodoForm(instance=todo)
#     context = {
#         'todo': todo,
#         'form' : form,
#     }

#     return render(request, 'todos/edit.html', context)


# def update(request, pk):
  
#     todo = Todo.objects.get(pk=pk)
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # todo.title = title
#     # todo.content = content
#     # todo.save()

#     # instance=todo로 인해서 거의 같은 식이지만 수정해야하는지 생성해야 하는지 판단 할 수 있음
#     form = TodoForm(request.POST, instance=todo)
#     if form.is_valid():
#         form.save()
#         return redirect('todos:detail', todo.pk)
#     context = {
#         'todo' : todo,
#         'form' : form,
#     }
#     return render(request, 'todos/edit.html', context)