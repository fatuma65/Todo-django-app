from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_todos, name='get_all_todos'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),

]