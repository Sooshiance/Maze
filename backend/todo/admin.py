from django.contrib import admin

from todo.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'active', 'status']
    list_filter = ['active', 'status']
