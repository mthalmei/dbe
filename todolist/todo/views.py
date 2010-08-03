from todolist.todo.models import *
from django.http import HttpResponseRedirect

def mark_done(request, pk):
    item = Item.objects.get(pk=pk)
    item.done = True
    item.save()
    return HttpResponseRedirect("/admin/todo/item/")
