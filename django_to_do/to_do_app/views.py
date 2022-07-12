from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from.models import Todo

# Create your views here.

def redir(request):
    return redirect('todos')

def index(request):
    data = { 'item_list': Todo.objects.all().values() }
    return render(request, 'to-do-app/todos.html', data)

def new(request):
    print('new: ', request.method)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        
        item = Todo(title=title, description=description, due_date=due_date)
        item.save()
        
        return redirect('see_item', id=item.id)
    
    if request.method == 'GET':
        return render(request, 'to-do-app/new.html')

def see_item(request, id):
    item = Todo.objects.filter(id=id).values()[0]
    details = {
        'id': id,
        'title': item['title'],
        'description': item['description'],
        'created_date': item['created_date'],
        'due_date': item['due_date'],
    }
    
    data = { 'item_list': [details] }
    
    return render(request, 'to-do-app/todos.html', data)

def edit(request, id):
    if request.method == 'GET':
        item = Todo.objects.get(id=id)
        details = {
            'id': id,
            'title': item.title,
            'description': item.description,
            'created_date': item.created_date,
            'due_date': item.due_date,
        }

        data = { 'item': details }

        return render(request, 'to-do-app/edit.html', data)
    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        
        item = Todo.objects.get(id=id)
        item.title = title
        item.description = description
        item.due_date = due_date
        
        item.save()
        
        return redirect('todos')

def delete(request, id):
    item = Todo.objects.get(id=id)
    item.delete()
    
    return redirect('todos')
    