import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1190592.xml'
print ("Retrieving", url)
html = urllib.request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount = len(results)
isum = 0

for result in results:
  isum += int(result.find('count').text)
print(icount)
print(isum)