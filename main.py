site='http://stankin.ru/university'
word='обработки'

import re
import requests
import time
pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+)"')
body_pattern=re.compile(r'<body>([\s\S]+)</body>')
style_pattern=re.compile(r'<style[a-zA-Z="/ ]*>[\S\s]+</style>')
script_pattern=re.compile(r'<script[a-zA-Z="/ ]*>[\s\S]+</script>')
nbsp_pattern=re.compile(r'&nbsp;')
hook_pattern=re.compile(r'<.*?>')
space_pattern=re.compile(r'[\t\n\r\s]+')
symbol_pattern=re.compile(r'[,.:+;!&%|\()/©@"?/]+')

def foo(search_word, addr, index):
  html=requests.get(addr).text
  links=pattern.findall(html)
  
  text=body_pattern.search(html).group()

  text=script_pattern.sub('',text)
  text=style_pattern.sub('',text)
  
  #print (text)
  #print ('---------------')
  text=hook_pattern.sub('',text)
  text=nbsp_pattern.sub('',text)
  text=space_pattern.sub(' ',text).lower()#AbC->abc
  #извращения с ненужными символами
  text=symbol_pattern.sub('',text)

  print (text)  
  print ('---------------')


  words=re.split(' ',text)
  for i in range(len(words))
    if words[i]=='':
    words.pop(i)
  print (words)
  print ('---------!!!-------')
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
