from dbe.blog.models import Post, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

class CommentAdmin(admin.ModelAdmin):
    display_fileds = ["post", "author", "created"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
