from django.shortcuts import redirect, render, get_object_or_404
from todos.models import TodoItem
from django.http import HttpResponse
from django.template import loader
from .forms import TodoItemForm

# Create your views here.
def get_all_todos(request):
    todos = TodoItem.objects.all().values()
    template = loader.get_template('allTodos.html')
    context = {
        'todos': todos
    }
    return HttpResponse(template.render(context, request))

def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        form.save()
        return redirect('get_all_todos')
    else:
        form = TodoItemForm()
    return render(request, 'add_todo.html', {'form': form})

def edit_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('get_all_todos')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'edit_todo.html', {'form':form})
    
def delete_todo(request, id):
    todo = TodoItem.objects.get(id=id)
    todo.delete()
    return redirect('get_all_todos')