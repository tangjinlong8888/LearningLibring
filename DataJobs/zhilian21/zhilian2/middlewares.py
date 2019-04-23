# -*- coding: utf-8 -*-
# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
from scrapy import signals
from scrapy.conf import settings
import pymysql
import scrapy
import random
import requests


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        ips = self.get_ip()
        ip = random.choice(ips)
        print('ip地址：',ip)
        request.meta['proxy'] = ip

    #从数据库中读取ip和port
    def get_ip(cls):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='spider',port=3306,charset='utf8')
        cursor = conn.cursor()
        sql = 'select ip,port from proxy_ip'
        cursor.execute(sql)
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        ips =[]
        for data in datas:
            proxy = 'http://'+data[0]+':'+data[1]
            ips.append(proxy)
        return ips

#选择随机user_agent
class UserAgentMiddleware(object):
    def __init__(self):
        self.user_agent = list(settings['USER_AGENT'])
    def process_request(self,request,spider):
        ua = random.choice(self.user_agent)
        # print('当前头部请求为：{}'.format(ua))
        request.headers.setdefault('User-Agent',ua)

class Zhilian2SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Zhilian2DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 为每个通过下载器中间件的请求调用。
        # 必须：
        # - 返回无：继续处理此请求
        # - 或返回响应对象
        # - 或返回请求对象
        # - or raise IgnoreRequest: 将调用已安装的下载器中间件的process_exception（）方法
        return None
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
