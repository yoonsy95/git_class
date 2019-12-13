#div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a > span.ah_k
#div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li.ah_item.ah_on > a > span.ah_k

import requests
from datetime import datetime
from bs4 import BeautifulSoup

url='https://www.naver.com/'
html=requests.get(url).text
soup=BeautifulSoup(html, 'html.parser')
names=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div > ul > li > a > span.ah_k')

now=datetime.now()
print(f'{now} 기준 실시간 검색어')

for name in names:
    print(name.text)
