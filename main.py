import re
import requests
pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+)"')
html=requests.get('http://stankin.ru').text
links=pattern.findall(html)
print(links)
