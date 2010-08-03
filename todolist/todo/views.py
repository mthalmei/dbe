from todolist.todo.models import *
from django.http import HttpResponseRedirect, HttpResponse

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

def onhold_done(request, mode, action, pk):
    """Toggle Done / Onhold on/off."""
    item = Item.objects.get(pk=pk)

    if mode == "onhold": attr = item.onhold
    elif mode == "done": attr = item.done


    if action == "on": attr = True
    else: attr = False
    
    if mode == "onhold": item.onhold = attr
    elif mode == "done": item.done = attr

    item.save()
    return HttpResponse('0')

