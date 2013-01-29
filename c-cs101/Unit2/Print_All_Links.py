# Referece http://forums.udacity.com/questions/30562/get_page-is-not-working

import urllib2

def get_page(url):
    try:
	return urllib2.urlopen(url).read()
    except:
	return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    #Insert your code below here
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

page=get_page('https://blog-junstrix.rhcloud.com/')

while True:
    url, endpos = get_next_target(page)
    if url:
	print url
	page = page[endpos:]
    else:
	break
