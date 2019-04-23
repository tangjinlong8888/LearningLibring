from Python_to_HDFS import wrtie_to_hdfs,mkdirs,client
from bs4 import BeautifulSoup
import requests
import re
url='https://www.baidu.com/'
res=requests.get(url)
a=url.split('/',1)
c=a[1].replace('.','/')
print(c)

mkdirs(client,c)
wrtie_to_hdfs(client,c+'/1.html',data=res.content.decode('utf8'))
# with open('1.html','w') as f :
#     f.write(res.content.decode('utf8'))
#
# print(res.content.decode('utf8'))
