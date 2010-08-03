from django.db import models
from django.contrib.auth.models import User

class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return unicode(self.datetime.strftime("%b %d, %Y, %H:%M"))

class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.ForeignKey(DateTime)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    onhold = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)
    progress = models.IntegerField(default=0)

    def progress_(self):
        return "<div style='width: 100px; border: 1px solid #ccc;'>" + \
                "<div style='height: 4px; width: %dpx; background: #555; '></div></div>" % self.progress
    progress_.allow_tags = True

    def delete(self):
        return "<a href='/item_action/delete/%d/'>Delete</a>" % self.pk
    delete.allow_tags = True

    def done_(self):
        if self.done:
            btn = "<div id='done_%s'><img class='btn' src='/media/img/admin/icon-yes.gif' /></div>"
        else:
            btn = "<div id='done_%s'><img class='btn' src='/media/img/admin/icon-no.gif' /></div>"
        return btn % self.pk
    done_.allow_tags = True
    done_.admin_order_field = "done"
    
    def onhold_(self):
        if self.onhold:
            btn = "<div id='onhold_%s'><img class='btn' src='/media/img/admin/icon-yes.gif' /></div>"
        else:
            btn = "<div id='onhold_%s'><img class='btn' src='/media/img/admin/icon-no.gif' /></div>"
        return btn % self.pk
    onhold_.allow_tags = True
    onhold_.admin_order_field = "onhold"

