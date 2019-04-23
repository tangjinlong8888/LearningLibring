import json
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import re

"""
模拟浏览器
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

"""
获得所有url
"""


def get_all_url(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except ConnectionError:
        return None


"""
解析url
"""


def parse_url(html):
    soup = BeautifulSoup(html, 'lxml')
    url_items = soup.select('#resultList .el .t1')
    url_items.pop(0)
    for url_item in url_items:
        all_a = url_item.find('span').find('a')
        yield all_a['href']


"""
处理url
"""


def deal_with_url(href_list):
    pattern = re.compile(r'.*?://jobs.*?t=0')
    urls = []
    for href in href_list:
        url_list = re.findall(pattern, href)
        if len(url_list) != 0:
            urls.append(url_list[0])
    return urls


"""
获得详情页url
"""


def get_detail_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except ConnectionError:
        return None


"""
详情页信息处理
"""


def parse_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    job = soup.select('.tHeader.tHjob .in .cn h1')[0]['title']
    salary = soup.select('.tHeader.tHjob .in .cn strong')[0].text
    company = soup.select('.tHeader.tHjob .in .cn .cname .catn')[0]['title']
    info = soup.select('.tHeader.tHjob .in .cn .msg.ltype')[0]['title'].replace('\xa0\xa0', '')
    info_list = info.split('|')
    location = info_list[0]
    exp = info_list[1]
    education = info_list[2]
    count = info_list[3]
    job_info_item = soup.select('.bmsg.job_msg.inbox')[0].text
    regx = re.compile(r'[A-Za-z]+')
    job_info = ','.join(re.findall(regx, job_info_item))
    yield {
        'title': job,
        'salary': salary,
        'address': company,
        'experience': exp,
        'education': education,
        'skill': job_info,
        'city': location,
        'people_num': count,
    }


"""
数据写进JSON文件
"""


def write_to_file(data):
    with open('Python2.json', 'a+', encoding='utf-8') as f:
        datas = json.dumps(data, ensure_ascii=False)
        f.write(datas + ',\n')
        f.close()


"""
爬虫启动函数
"""


def main(offset):
    print('正在抓取', offset)
    url = 'https://search.51job.com/list/010000%252C020000%252C030200%252C040000%252C090200,000000,0000,00,9,99,Python,2,' \
          + \
          str(offset) + \
          '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    url_html = get_all_url(url)
    if url_html:
        href_list = parse_url(url_html)
        urls = deal_with_url(href_list)
        for url1 in urls:
            detail_html = get_detail_html(url1)
            if detail_html:
                details = parse_detail(detail_html)
                for detail in details:
                    # print(detail)
                    write_to_file(detail)


if __name__ == '__main__':
    """
    多线程启动
    """
    pool = Pool()
    pool.map(main, [i for i in range(1, 2001)])
