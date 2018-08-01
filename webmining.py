import urllib.request
# from bs4 import BeautifulSoup
import os
import html
import re
from goose3 import Goose

url = input('Enter a url, followed by a space: ')
url = url.replace(' ','')

try:
     page = urllib.request.urlopen(url, data=None)

except urllib.error.HTTPError as e:
     print('Request failed. Error Code {}'.format(e.getcode()))
     exit()

except (urllib.error.URLError, ValueError):
     print('An error has occured, please try again')
     exit()

print('Status code: ' + str(page.getcode()))

# soup = BeautifulSoup(page, 'html.parser')

g = Goose()
article = g.extract(url=url)
print(article.cleaned_text)




'''def cleanhtml(raw_html):
  beginning = re.compile('\A.*?<p class="zn-body__paragraph speakable">')
  cleanbeg = re.sub(beginning, '', raw_html)

  end = re.compile('zn-body__footer.*?\Z')
  cleanend = re.sub (end, '', cleanbeg)

  print(cleanend)

  #cleanr = re.compile('<.*?>')
  # cleanspan = re.compile('<span.*?</span>')
  #vcleanrelated = re.sub(cleanspan, '', raw_html)
  # cleantext = re.sub(cleanr, '', article)
  # cleantext = cleantext.replace(' , ', '')
  # print(cleantext)

cleanhtml(rep)

print(article)'''