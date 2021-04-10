from django.contrib import admin
from .models import *


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('content', 'created', 'important')
    list_filter = ['created']
    search_fields = ['content']
    fieldsets = [
        ('Creation date information', {'fields': ['created']}),
        ('Content of a to-do element', {'fields': ['content']}),
        ('Importance', {'fields': ['important']})
    ]


admin.site.register(ToDoItem, ToDoItemAdmin)