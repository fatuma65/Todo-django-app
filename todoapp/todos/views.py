from django.shortcuts import redirect, render, get_object_or_404
from todos.models import TodoItem
from django.http import HttpResponse
from django.template import loader
from .forms import TodoItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm
# Create your views here.
def get_all_todos(request):
    todos = TodoItem.objects.filter(user=request.user)
    template = loader.get_template('allTodos.html')
    context = {
        'todos': todos
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('get_all_todos')
    else:
        form = TodoItemForm()
    return render(request, 'add_todo.html', {'form': form})

@login_required
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
    
@login_required
def delete_todo(request, id):
    todo = TodoItem.objects.get(id=id)
    todo.delete()
    return redirect('get_all_todos')

def loginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('get_all_todos')
    else:
        print('invalid username and password')
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registerView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loginView')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    return render(request, 'base.html')
