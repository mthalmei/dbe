from django.conf.urls.defaults import *

urlpatterns = patterns('dbe.blog.views',
   (r"^$", "main"),
   (r"^(\d+)/$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
)

