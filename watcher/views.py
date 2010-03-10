from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings

import datetime #use to parse time
import urllib
try:
    import simplejson #seems to already be installed...
except ImportError:
    from django.utils import simplejson
import feedparser #use _sanitizeHTML

from watcher.models import WatchedUrl, Post
from watcher.forms import AddURLForm

# Create your views here.
def home(request):
    #Get JSON data of RSS feed:
    watched_urls = WatchedUrl.objects.all() #need to get the full object
    
    for each_wu in watched_urls:
        #Encode the URI so that the key=value pairs don't get parsed in the Google url:
        url = urllib.quote(each_wu.url)
        
        #TODO: Differentiate between first import and subsequent imports. We do not
        #      need num=-1 and scoring=h for subsequent imports.
        gfeed_url = 'http://ajax.googleapis.com/ajax/services/feed/load?q=' + \
                    url + \
                    '&v=1.0&num=-1&scoring=h' + \
                    '&key=' + settings.GOOGLE_FEEDS_API_KEY
                    #The above key is for localhost only.
        json_result = urllib.urlopen(gfeed_url)

        #Parse the JSON string into python data structures:
        result = simplejson.loads(json_result.read()) #Use read() to return string
        entries = result['responseData']['feed']['entries']
        
        skip_count = 0
        for entry in entries:
            #Parse the date. We remove the last part which is the time offset since
            #python's support for parsing it is highly variable:
            temp = entry['publishedDate'].split()
            date_no_offset = ' '.join(temp[0:-1]) #remove the last field 
            dt = datetime.datetime.strptime(date_no_offset, 
                                            '%a, %d %b %Y %H:%M:%S')

            #Sanitize the HTML
            #Not necessarily needed. We can trust that both CL and Google Feeds do
            #some level of sanitization.
            entry['title'] = feedparser._sanitizeHTML(entry['title'], 'utf-8')
            entry['content'] = feedparser._sanitizeHTML(entry['content'], 'utf-8')

            #Put in database. To prevent duplicates, try to get the url first from
            #database:
            try:
                post = Post.objects.get(link = entry['link'])
                #If the post already exists, then skip it.
                skip_count += 1
                if skip_count >= settings.DUPLICATE_POSTS_THRESHOLD:
                    break #we don't need to keep updating anymore
                continue
            except Post.MultipleObjectsReturned:    
                #Technically, this shouldn't happen if other code works
                continue #skip creating new entry
            except Post.DoesNotExist:
                #Create a new entry
                post = Post()
            post.watched_url = each_wu
            post.date = dt
            post.title = entry['title']
            #post.content = pickle.dumps(entry) 
            post.content = entry['content']
            post.link = entry['link']
            post.save()

    #Now select the entries in chronological order
    entries = Post.objects.order_by('-date') #DESC order

    #Create add url form:
    add_url_form = AddURLForm()
        
    return render_to_response('home.html', {'entries': entries, 
                                            'add_url_form': add_url_form, })

def add(request):
    if request.method == 'POST':
        form = AddURLForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data['url']+'&format=rss'

            #We are currently assuming that the url passed in is encoded.
            wu = WatchedUrl()
            wu.url = url
            #Set last_checked to a date a long, long time ago so that it will
            #immed. update
            wu.last_checked = datetime.datetime(1900, 1, 1, 1, 1)
            wu.save()
            
            return render_to_response('added.html', {'added_url': url})
    else:
        form = AddURLForm()

    
    #return render_to_response('added.html', {'added_url': url, })
    return render_to_response('add.html', {'form': form})

def delete(request, url_id):
    #If the url_id to delete is submitted...
    if url_id >= 0 and url_id != None:
        try:
            url_to_delete = WatchedUrl.objects.get(id = url_id)
            #Delete all posts associated with this url
            associated_posts = Post.objects.filter(watched_url = url_to_delete)
            associated_posts.delete()
            deleted_url = url_to_delete.url
            url_to_delete.delete()
            return render_to_response('deleted.html', {'deleted_url': deleted_url, })
        except WatchedUrl.DoesNotExist:
            pass #display the page to delete urls
            #return HttpResponseRedirect('/')

    #Otherwise, display the list of urls to delete
    watched_urls = WatchedUrl.objects.all()
    
    return render_to_response('delete.html', {'watched_urls': watched_urls})

