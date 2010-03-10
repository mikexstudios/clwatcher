from django.db import models

# Create your models here.

class WatchedUrl(models.Model):
    #id is auto-defined and auto-incrementing
    url = models.CharField(max_length = 500) 
    last_checked = models.DateTimeField()

    def __unicode__(self):
        '''Used when print is called on this object.'''
        return self.url

class Post(models.Model):
    #id is auto-defined and is auto-incrementing
    watched_url = models.ForeignKey(WatchedUrl)
    date = models.DateTimeField()
    title = models.CharField(max_length = 500)
    content = models.TextField()
    link = models.CharField(max_length = 200)
    #new = models.BooleanField()
    #A better way of defining the field of content would be to create a
    #PickledField class which handles the pickling of data.
    #content = models.TextField() 
    
    def __unicode__(self):
        '''Used when print is called on this object.'''
        return str(self.id)
