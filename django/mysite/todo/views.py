from django.shortcuts import render, redirect
from .models import Todo

def index(request):
   todos = Todo.objects.all()
   return render(request, 'index.html', {'todos': todos})

def addTodo(request):
   todo = Todo(text=request.POST['text'])
   todo.save()
   return redirect('/todos')

def deleteTodo(request, id):
   todo = Todo.objects.filter(id=id)
   todo.delete()
   return redirect('/todos')