from django.shortcuts import render, get_object_or_404
from todos.models import TodoList

# Create your views here.


def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list_list": todo_list,
    }
    return render(request, "todos/todolist.html", context)


def todo_list_detail(request, id):
    todo_list_detail = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": todo_list_detail,
    }
    return render(request, "todos/detail.html", context)
