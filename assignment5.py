import urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_1190593.json'
print('Retrieving', url)
response = urllib.request.urlopen(url)
js = response.read().decode()
data = json.loads(js)
print('Retrieved', len(js), 'characters')
char = 0
sum = 0

for item in data['comments']:
  sum += int(item['count'])

print(sum)