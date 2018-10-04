import re
import requests
pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+)"')
html=requests.get('http://stankin.ru').text
links=pattern.findall(html)
namesite = ''
i=0
list(set(links))
for item in links:
  if (item > 'http://')&(item[:i-1]!=namesite):
    namesite = 'http://'
    i = 7
    while item[i]!='/':
      namesite += item[i]
      i+=1
    print(item)
  else:
    print(namesite+item)
