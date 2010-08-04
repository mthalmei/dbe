from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from dbe.blog.models import *
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
import time

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    for post in posts.object_list:
        post.num_comments = Comment.objects.filter(post=post).count()

    return render_to_response("list.html", dict(posts=posts, post_list=posts.object_list, user=request.user, months=mkmonth_lst()))

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def post(request, pk):
    """Single post with comments and a comment form"""
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, user=request.user, comments=comments, form=CommentForm())
    d.update(csrf(request))
    return render_to_response("post.html", d)

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]:
            author = p["author"]
        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect("/blog/%s/" % pk)

def mkmonth_lst():
    """Make a list of months to show archive links."""

    if not Post.objects.count(): return []

    # set up vars
    year, month = time.localtime()[:2]
    first = Post.objects.order_by("created")[0]
    fyear = first.created.year
    fmonth = first.created.month
    months = []
    mnames = "January February March April May June July August September October November December"
    mnames = mnames.split()

    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 11, -1
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, mnames[m-1]))
    return months

def month(request, year, month):
    """Monthly archive."""
    posts = Post.objects.filter(created__year=year, created__month=month)
    return render_to_response("list.html", dict(post_list=posts, user=request.user, months=mkmonth_lst(), archive=True))


def delete_comment(request, pk=None):
    """Delete comment(s) with primary key 'pk' or with pks in POST."""
    if request.user.is_staff:
        if not pk: pklist = request.POST.getlist("delete")
        else: pklist = [pk]

        for pk in pklist:
            Comment.objects.filter(pk=int(pk)).delete()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
