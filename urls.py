from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dbe/', include('dbe.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^item_action/(done|delete|onhold)/(\d*)/$', "dbe.todo.views.item_action"),
    (r"^onhold_done/(onhold|done)/(on|off)/(\d*)/$", "dbe.todo.views.onhold_done"),
    (r"^progress/(\d*)/$", "dbe.todo.views.progress"),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('dbe.blog.urls')),
)
