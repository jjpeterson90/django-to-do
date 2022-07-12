from django.urls import path
from . import views

# app_name = 'todos'

urlpatterns = [
    path('', views.redir),
    path('todos', views.index, name='todos'),
    path('todos/new', views.new, name='new'),
    path('todos/<int:id>', views.see_item, name='see_item'),
    path('todos/<int:id>/edit', views.edit, name='edit'),
    path('todos/<int:id>/delete', views.delete, name='delete'),
]
