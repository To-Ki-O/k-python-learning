from django.contrib import admin
from django.urls import include, path
from todo.views import index, addTodo, deleteTodo

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', index),
    path('todos', index),
    path('todos/add', addTodo),
    path('todos/delete/<int:id>', deleteTodo),
]
