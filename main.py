site='http://stankin.ru/university'
word='адрес'

import re
import requests
import time
pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+)"')
body_pattern=re.compile(r'<body>([\s\S]+)</body>')
script_pattern=re.compile(r'<script[\S\s]*>[\s\S]+</script>')
hook_pattern=re.compile(r'<[a-z/="0-9 -]+>')
space_pattern=re.compile(r'[\t\n\r\s]+')


def foo(search_word, addr, index):
  html=requests.get(addr).text
  links=pattern.findall(html)
  
  text=body_pattern.search(html).group()
  
  text=script_pattern.sub('',text)
  print (text)
  text=re.sub('&nbsp;','',text)
  text=space_pattern.sub(' ',text).lower()#AbC->abc
  
  text=hook_pattern.sub('',text)
  
  #text=space_pattern.sub(' ',text).lower()#AbC->abc
  words=re.split(' ',text)
  if words[0]=='':
    words.pop(0)
  if words[len(words)-1]=='':
    words.pop(len(words)-1)
  #print (words)
  repetitions=0
  list_rep=[]
  for item in words:
    if item==search_word:
      repetitions+=1
  list_rep.append(repetitions)
  print (list_rep) 



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
    current_links = foo(search_word,item,index-1)
    all_links.extend(current_links)
  new_links.extend(all_links)
  return new_links

for item in foo(word,site,2):
  print (item)
