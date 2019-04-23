# -*- coding: utf-8 -*-
import scrapy
import requests
from zhilian2.items import XiciItem
from scrapy.conf import settings
import pymysql
import time


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/wt/1']

    #基础网址
    base_url = 'https://www.xicidaili.com/wt/'
    start = 1
    def parse(self, response):
        #xpath提取数据节点列表
        node_list = response.xpath('//tr[@class="odd"]|//tr[@class=""]')

        for node in node_list:
            #实例化item类
            item1 = XiciItem()
            #将ip地址数据赋值给item
            item1['ip'] = node.xpath('./td[2]/text()').extract_first()
            #将端口数据赋值给port
            item1['port'] = node.xpath('./td[3]/text()').extract_first()
            #将速度数据赋值给speed
            item1['speed'] = node.xpath('./td[7]/div/@title').extract_first()
            #将类型数据赋值给proxy_type
            item1['proxy_type'] = node.xpath('./td[6]/text()').extract_first()

            proxies = {
                "http":item1['ip']+':'+item1['port']
            }
            try:
                if requests.get('http://www.baidu.com',proxies=proxies,timeout=2).status_code == 200:
                    if requests.get('http://www.hao123.com',proxies=proxies,timeout=2).status_code == 200:
                        print('prase_成功的ip地址:{}'.format(item1['ip']+':'+item1['port']))
                        yield item1
                    else:
                        print('parse_失败的IP地址:{}'.format(item1['ip'] + ':' + item1['port']))
            except:
                print('parse_失败的IP地址:{}'.format(item1['ip']+':'+item1['port']))

        self.start += 1
        #构造下一页链接，爬取20页
        if self.start <= 20:
            next_page = self.base_url + str(self.start)
        try:
            yield scrapy.Request(url=next_page,callback=self.parse)
        except:
            print('西刺代理数据爬取完成！')

