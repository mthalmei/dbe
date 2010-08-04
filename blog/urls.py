from django.conf.urls.defaults import *

urlpatterns = patterns('dbe.blog.views',
   (r"^$", "main"),
   (r"^(\d+)/$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
   (r"^month/(\d+)/(\d+)/$", "month"),
   (r"^delete_comment/(\d+)/$", "delete_comment"),
   (r"^delete_comment/$", "delete_comment"),
)

