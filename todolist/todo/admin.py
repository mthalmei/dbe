from django.contrib import admin
from todolist.todo.models import Item, DateTime

from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "created", "done", "mark_done", "onhold", "toggle_onhold"]
    search_fields = ["name"]
    list_filter = ["priority", "difficulty", "onhold", "done"]

class ItemInline(admin.TabularInline):
    model = Item

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInline]

    def response_add(self, request, obj, post_url_continue='../%s/'):
        """ Determines the HttpResponse for the add_view stage.  """
        opts = obj._meta
        pk_value = obj._get_pk_val()

        msg = "Item(s) were added successfully."
        # Here, we distinguish between different save types by checking for
        # the presence of keys in request.POST.
        if request.POST.has_key("_continue"):
            self.message_user(request, msg + ' ' + _("You may edit it again below."))
            if request.POST.has_key("_popup"):
                post_url_continue += "?_popup=1"
            return HttpResponseRedirect(post_url_continue % pk_value)

        if request.POST.has_key("_popup"):
            return HttpResponse(
              '<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");'
              '</script>' % (escape(pk_value), escape(obj)))
        elif request.POST.has_key("_addanother"):
            self.message_user(request, msg + ' ' + (_("You may add another %s below.") %
                                                    force_unicode(opts.verbose_name)))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)

            return HttpResponseRedirect("/admin/todo/item/")

admin.site.register(Item, ItemAdmin)
admin.site.register(DateTime, DateAdmin)
