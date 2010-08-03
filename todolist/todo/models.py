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


    def mark_done(self):
        return "<a href='/mark_done/%d/'>Done</a>" % self.pk
    mark_done.allow_tags = True
    
    def toggle_onhold(self):
        return "<a href='/toggle_onhold/%d/'>Toggle OnHold</a>" % self.pk
    toggle_onhold.allow_tags = True
