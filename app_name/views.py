from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem
from django.contrib import messages


def to_do_view(request):
    all_to_do_items = ToDoItem.objects.all().order_by('-important', 'completed')
    return render(request, 'to_do_list.html', {'all_items': all_to_do_items})


def add_to_do(request):
    new_item = ToDoItem(content=request.POST['content'])
    new_item.save()
    messages.info(request, 'Задача добавлена')
    return HttpResponseRedirect('/todo/')


def delete_to_do(request, todo_id):
    item_to_delete = ToDoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    messages.info(request, 'Задача удалена')
    return HttpResponseRedirect('/todo/')


def is_important(request, todo_id):
    if not ToDoItem.objects.get(id=todo_id).important:
        ToDoItem.objects.filter(id=todo_id).update(important=True)
    else:
        ToDoItem.objects.filter(id=todo_id).update(important=False)

    return HttpResponseRedirect('/todo/')


def is_completed(request, todo_id):
    if not ToDoItem.objects.get(id=todo_id).completed:
        ToDoItem.objects.filter(id=todo_id).update(completed=True)
        ToDoItem.objects.filter(id=todo_id).update(important=False)
    else:
        ToDoItem.objects.filter(id=todo_id).update(completed=False)

    return HttpResponseRedirect('/todo/')


def delete_completed(request):
    ToDoItem.objects.filter(completed__exact=True).delete()
    messages.info(request, 'Удалены все выполненные задачи')
    return HttpResponseRedirect('/todo/')


def delete_all(request):
    ToDoItem.objects.all().delete()
    messages.info(request, 'Удалены все задачи')
    return HttpResponseRedirect('/todo/')


def redirect_edit(request, todo_id, todo_content):
    return render(request, 'edit.html', {'todo_id': todo_id,
                                         'todo_content': todo_content})


def edit(request, todo_id):
    ToDoItem.objects.filter(id=todo_id).update(content=request.POST['content'])
    return HttpResponseRedirect('/todo/')