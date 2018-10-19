site='http://stankin.ru/university/'
import re
import requests
import time
pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+)"')
body_pattern=re.compile(r'<body>([\s\S]+)</body>')
script_pattern=re.compile(r'<script[\S\s]*>[\s\S]+</script>')
hook_pattern=re.compile(r'<[\S ]+>')
space_pattern=re.compile(r'[\t\n\r\s]+')


def foo(addr, index):
  html=requests.get(addr).text
  links=pattern.findall(html)

  body_text=body_pattern.search(html)

  script_text=script_pattern.sub('',body_text)
  hook_text=hook_pattern.sub('',script_text)
  
  #space_text=space_pattern.split(text)
  print (hook_text)
 # print (space_text)
  new_links=[]
  
  for item in links:
    if item.endswith(('.png','.css')):
      continue
    if item.startswith('/'):
      new_links.append (site+item)
    elif not item.startswith('/') and not item.startswith('http://'):
      new_links.append (addr+'/'+item) 
    elif 'stankin.ru' in item:
      new_links.append(item)
    if (index-1<0):
      return new_links
  all_links =[]
  for item in new_links:
    print(item)
    time.sleep(2)
    current_links = foo(item,index-1)
    all_links.extend(current_links)
  new_links.extend(all_links)
  return new_links
for item in foo(site,2):
  print (item)
