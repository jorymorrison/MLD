import urllib.request
import os
from goose3 import Goose
from goose3.configuration import Configuration

url = input('Enter a url, followed by a space: ')
url = url.replace(' ','')

try:
     page = urllib.request.urlopen(url, data=None)

# error thrown if the status code is bad
except urllib.error.HTTPError as e:
     print('Successfully Retrieved Status Code: ' + e.getcode())
     print('Failed to Retrieve Representation')
     exit()

# error thrown if the URL is bad
except (urllib.error.URLError, ValueError):
     print('Failed to Retrieve Status Code')
     exit()

scode = str(page.getcode())

print('Successfully Retrieved Status Code: ' + scode)
print('Successfully Retrieved Representation')

log = open('log.txt', 'a+')
path = 'C:\ Users\Libster\Documents\GitHub\MLD'
path = path.replace(' ', '')

print('Successfully Created Log File At: ' + path)

log.write('Status Code: ' + scode)

print('Successfully Wrote Retrieval Status to Log')

g = Goose()
# g.config.known_context_patterns = {'attr': 'class', 'value': 'l-container'}
article = g.extract(url=url)
# article.strict = False
titletext = (article.title)
bodytext = article.cleaned_text
bodytext = bodytext.replace('"', "'")
# print(bodytext)

serialized = '{\n   "article": {\n   "title": "' + titletext + '",\n   "body": "' + bodytext + '"\n  }\n}'

log.write(serialized)

print('Successfully Wrote Retrieval to Log')

log.close()