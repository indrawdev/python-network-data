import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter URL : ')
count = int(input('Enter Count : '))
pos = int(input('Enter Position : '))

def parseHtml(url, pos):
  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  i = 0
  for tag in tags:
    i += 1
    if i == pos:
      return tag.get('href', None)

current_num = 0
while current_num < count:
  print('Retrieving: ', url)
  url = parseHtml(url, pos)
  current_num += 1

print(url)