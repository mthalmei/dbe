from django.contrib import admin
from todolist.todo.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "created", "done"]
    search_fields = ["name"]

admin.site.register(Item, ItemAdmin)
