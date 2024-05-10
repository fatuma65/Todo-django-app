from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('todos/', views.get_all_todos, name='get_all_todos'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('todos/delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('register/', views.registerView, name='signup'),
]