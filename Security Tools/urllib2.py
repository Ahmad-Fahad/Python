# kaj korche na

import urllib2
request = urllib2.Request('https://docs.python.org/')
response = urllib2.urlopen(request)
payload = response.read()
print(payload)