#!/usr/bin/env python

"""
times news wire!

http://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=etc
example for tech:
http://api.nytimes.com/svc/news/v3/content/all/technology.json?api-key=?

format is:
http://api.nytimes.com/svc/news/{version}/content/{source}/{section}[/time-period][.response-format]?api-key={your-API-key}

SDC 9/17/2010

"""

import simplejson
import urllib2

NYT_API_KEY = '' # GET YOUR OWN KEY! (and put it here)
NYT_URL = 'http://api.nytimes.com/svc/news/v3/content/all/%s.json?api-key=%s'

def grab_news(category = 'all',api_key = NYT_API_KEY):
    object = {"results": ['News Site UNAVAILABLE']}
    try:
        raw = urllib2.urlopen(NYT_URL %(category,api_key))
        object = simplejson.loads(raw.read())
    except Exception:
        pass
    return object

if __name__ == '__main__':
    data = grab_news()
    for res in data['results']:
        print "%s\n" % res['title']
        
