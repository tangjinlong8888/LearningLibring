import queue

import requests
from bs4 import BeautifulSoup
from requests.exceptions import SSLError
from Python_to_HDFS import Client_hdfs,write_to_hdfs,mkdirs

import pymongo
client=pymongo.MongoClient(host='10.2.1.60',port=27017)
db=client.project
url='http://www.jobbole.com/'
LIMIT='jobbole'
url_list=list()
url_queue=queue.Queue()
def get_url(url):
    re=requests.get(url)
    re_text=re.text
    re_text_enconde=re_text.encode('utf-8')
    re_text=re_text_enconde.decode('utf-8')

    soup=BeautifulSoup(re_text)
    c=soup.find_all('a')
    for a in c :
        try:
            if a['href'] not in url_list and LIMIT in a['href']:
                url_list.append(a['href'])
                url_queue.put(a['href'])
        except KeyError:
            pass
def parse_url(url):
    return get_url(url)

url_queue.put(url)
while not url_queue.empty():
    url=url_queue.get()
    print(url)
    with open('url.txt','a+') as f:
        f.write(url+'  \r\n')
    try:
        parse_url(url)
    except Exception as e:
        print(e)


print(url_list)

