import queue
import pymongo
from Python_to_HDFS import Client_hdfs, wrtie_to_hdfs, mkdirs
import requests
from bs4 import BeautifulSoup
from config import MONGO_CLIENT

# 连接MongoDB(本地远程皆可)
mongo_client = pymongo.MongoClient(host=MONGO_CLIENT.get('HOST'), port=MONGO_CLIENT.get('PROT'))
# 捕捉异常
try:
    # 新建一个数据库search
    db = mongo_client.search_one
    # 新建集合 col
    collection = db.col_one1
except Exception:
    pass

LIMIT = 'top'
not_include1 = 'comment'
not_include2 = 'reply'
# 设定一个入口地址
url = 'http://top.jobbole.com/'
# 创建一个列表list_url
list_url = [url, ]
# 创建一个列表queue_url
queue_url = queue.Queue()
# 向列表中添加url
queue_url.put(url)
# 创建一个字dian
temp_dict = {}
# 定义一个k
k = 1


# 写一个函数
def crawl():
    while queue_url:
        # 把设置为全局变量
        global k
        # 从queue_url中取出url 赋值给url
        url = queue_url.get()
        print(url)
        # try:
        try:
            # 获取URL的html内容
            res = requests.get(url, timeout=10)
        except Exception as e:
            print(e)
            continue

        # 把res输出成text格式
        res_text = res.text
        soup = BeautifulSoup(res_text, features="html.parser")
        try:
            title = soup.title.text
            temp_dict['title'] = title
        except Exception as e:
            print(e)
            continue

        try:
            content_list = list(soup.body.stripped_strings)[:-5]
            temp_dict['content'] = ''
            temp_dict['search_content'] = ''

        except Exception as e:
            print(e)
            continue
        hadoop_path = Client_hdfs.get('DIR')+'/{}.txt'.format(k)
        hadoop_dir = Client_hdfs.get('DIR')
        temp_dict['_id'] = k
        k = k + 1
        temp_dict['path'] = hadoop_path
        temp_dict['click'] = 0
        temp_dict['url'] = url

        collection.insert(temp_dict)
        try:
            mkdirs(Client_hdfs, hadoop_dir)
        except Exception as e:
            print(e)
            continue
        try:
            content = url + '\n' + title + '\n' + ' '.join(content_list)
            print(content)
            wrtie_to_hdfs(Client_hdfs, hadoop_path, content)
        except Exception:
            pass
            continue
        a = soup.find_all('a')
        for i in a:
            try:
                url = i.get('href', None)
                if url and LIMIT in url and url not in list_url and not_include1 not in url and not_include2 not in url:
                    list_url.append(url)
                    queue_url.put(url)
            except Exception as e:
                print(e)
                continue
if __name__ == '__main__':
    crawl()
