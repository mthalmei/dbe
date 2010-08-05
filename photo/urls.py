from django.conf.urls.defaults import *

urlpatterns = patterns('dbe.photo.views',
   (r"^$", "main"),
   (r"^(\d+)/$", "album"),
   (r"^image/(\d+)/$", "image"),
)

