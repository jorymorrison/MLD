import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import os
import html
import re
from goose3 import Goose
from goose3.configuration import Configuration

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

soup = BeautifulSoup(page, 'html.parser')

'''paragraphs = soup.find_all(attrs={'class': 'l-container'})
# print(paragraphs)
text = b" ".join([ paragraphs[4].text.encode('utf-8')])
print(text)'''


g = Goose()
g.config.known_context_patterns = {'attr': 'class', 'value': 'l-container'}
del g.config.known_context_patterns[1:]
print(g.config.known_context_patterns)
article = g.extract(url=url)
# article.strict = False
titleforsave = (article.title)
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