from todolist.todo.models import *
from django.http import HttpResponseRedirect

def mark_done(request, pk):
    item = Item.objects.get(pk=pk)
    item.done = True
    item.save()
    return HttpResponseRedirect("/admin/todo/item/")

def toggle_onhold(request, pk):
    item = Item.objects.get(pk=pk)
    if item.onhold:
        item.onhold = False
    else:
        item.onhold = True
    item.save()
    return HttpResponseRedirect("/admin/todo/item/")
