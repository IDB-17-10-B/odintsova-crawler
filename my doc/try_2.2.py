site='http://stankin.ru'
depth=2

import re
import requests
import time
pattern=re.compile(r'href="(?P<url>[a-zA-Z0-9:/&?=/.-]+">[a-zA-Zа-яА-Я0-9:/&?=/.-/ ]+)</a>')



def foo(addr, index):
  html=requests.get(addr).text
  links=pattern.findall(html)
  new_links=[]
  new_text=[]
  for item in links:
    if item.endswith(('.png','.css')):
      continue

    item_split=re.split(r'">',item,1)
    if len(item_split)>1:
     new_text.append(item_split[1])
    else:
      new_text.append('none')

    if item.startswith('/'):
      new_links.append (site+item_split[0])
    elif not item.startswith('/') and not item.startswith('http://'):
      new_links.append (addr+'/'+item_split[0]) 
    elif 'stankin.ru' in item:
      new_links.append(item_split[0])

  if (index-1<0):
    new_file=[new_links,new_text]
    return new_file

  all_links=[]
  all_text=[]
  item=1
  while item<len(new_links):
    print(new_text[item],'-',new_links[item])
    time.sleep(2)
    current_file = foo(item,index-1)
    all_links.extend(current_file[0])
    all_text.extend(current_file[1])
    item+=1
  new_links.extend(all_links)
  new_text.extend(all_text)
  new_file=[new_links,new_text]
  return new_file

main_file=foo(site,depth)
main_links.extend(main_file[0])
main_text.extend(main_file[1])
item=1
while item<len(main_links):
  print (main_text[item],'-',main_links[item])
  item+=1
