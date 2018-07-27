import urllib.request
from bs4 import BeautifulSoup
import requests
import os

url = input('Enter a url, followed by a space: ')
url = url.replace(' ','')


''' try:
    r = requests.get(url)
except:
     print ('An error occured, please try again.')
     exit()

print ('Status code: ' + str(r.status_code))

 if r.status_code != 200:
     print('Request failed. Error Code {}'.format(r.status_code))
     os.execv('/webminingtest.py') '''

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
test = soup.find_all('p')
print(test)