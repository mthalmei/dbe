from django.conf.urls.defaults import *

urlpatterns = patterns('dbe.photo.views',
   (r"^$", "main"),
   (r"^(\d+)/$", "album"),
)

