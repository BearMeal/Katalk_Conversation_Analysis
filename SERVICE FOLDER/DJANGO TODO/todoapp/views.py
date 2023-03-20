from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(req):
    todos=Todo.objects.filter(completed=False)
    return render(req, 'todoapp/todo_list.html', {'todos':todos})

def todo_detail(req,pk):
    todo=Todo.objects.get(id=pk)
    return render(req, 'todoapp/todo_detail.html', {'todo':todo})

def todo_post(req):
    if req.method == 'POST':
        form = TodoForm(req.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    
    else:
        form = TodoForm()
        return render(req, 'todoapp/todo_post.html', {'form':form})

def todo_edit(req, pk):
    todo=Todo.objects.get(id=pk)
    if req.method == 'POST':
        form = TodoForm(req.POST, instance=todo)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    
    else:
        form = TodoForm(instance=todo)
        return render(req, 'todoapp/todo_post.html', {'form':form})