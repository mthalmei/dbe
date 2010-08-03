from todolist.todo.models import *
from django.http import HttpResponseRedirect

def item_action(request, action, pk):
    """Mark done, toggle onhold or delete a todo item."""
    if action == "done":
        item = Item.objects.get(pk=pk)
        item.done = True
        item.save()
    elif action == "onhold":
        item = Item.objects.get(pk=pk)
        if item.onhold: item.onhold = False
        else: item.onhold = True
        item.save()
    elif action == "delete":
        Item.objects.filter(pk=pk).delete()

    return HttpResponseRedirect("/admin/todo/item/")

