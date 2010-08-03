from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^todolist/', include('todolist.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^mark_done/(\d*)/$', "todolist.todo.views.mark_done"),
    (r'^toggle_onhold/(\d*)/$', "todolist.todo.views.toggle_onhold"),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
