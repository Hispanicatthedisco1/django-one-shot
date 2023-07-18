from django.contrib import admin
from .models import TodoList

# Register your models here.
@admin.register(TodoList)

class TodosListAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
