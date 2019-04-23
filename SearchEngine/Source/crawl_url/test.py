import queue

import requests
from bs4 import BeautifulSoup
LIMIT='jobbole'
url='http://www.jobbole.com'
list_url=[url,]
queue_url=queue.Queue()
queue_url.put(url)
def crawl():
    while queue_url:
        url=queue_url.get()
        print(url)
        res=requests.get(url)
        res_text=res.text
        soup=BeautifulSoup(res_text)
        try:
            title=soup.title.text
        except Exception:
            continue
        # TODO:PUT INTO MONGODB
        try:
            content_list=list(soup.body.stripped_strings)[:-5]
            hadoop_path='******'
        except Exception:
            continue
        # TODO:save into hadoop
        a=soup.find_all('a')
        for i in a:
            try:
                url=i.get('href',None)
                if url and LIMIT in url and url not in list_url:
                    list_url.append(url)
                    queue_url.put(url)
            except Exception as e:
                print(e)








crawl()


# res=requests.get(url)
# res_text=res.text
# html=BeautifulSoup(res_text)
# b=html.title.text
# print(b)
# c=html.body
# a=c.stripped_strings
# print(a)
# print(list(a)[:-5])


# with open('a.txt','w',encoding='utf-8') as f:
#     f.write(a)

# print(type(a))
# print(html.get_text())
