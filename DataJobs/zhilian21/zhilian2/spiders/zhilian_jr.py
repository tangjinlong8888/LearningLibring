# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from scrapy.conf import settings

class ZhilianJrSpider(scrapy.Spider):

    name = 'zhilian_jr'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E9%87%91%E8%9E%8D&kt=3&_v=0.24269405&x-zp-page-request-id=547349d349054a5990999a946fbdf58f-1553767441033-132396']
    starts = 0
    def parse(self, response):
        data = response.text
        try:
            data = json.loads(data)
        except:
            print("找不到网页，请换IP地址或请求头部再试！")
        result = jsonpath.jsonpath(data, '$..results[*]')
        try:
            for node in result:
                # 实例化item对象
                item = Zhilian2Item()
                #将岗位名称数据赋值给jobname
                item['jobname'] = node['jobName']
                item['companyname'] = node['company']['name']
                # 将获取的字典类型的值转化成list
                value = list((node['company']['size']).values())
                item['companysize_code'] = value[0]
                item['companysize'] = value[1]
                value = list((node['company']['type']).values())
                item['companytype_code'] = value[0]
                item['companytype'] = value[1]
                value = list((node['workingExp']).values())
                item['workingexp_code'] = value[0]
                item['geo_lon'] = node['geo']['lon']
                item['geo_lat'] = node['geo']['lat']
                item['money'] = node['salary']
                item['city'] = node['city']['display'].split('-')[0]
                item['edulevel'] = node['eduLevel']['name']
                item['empltype'] = node['emplType']
                item['workingexp'] = node['workingExp']['name']
                # item['jobtag'] = json.dumps(node['welfare'],ensure_ascii=False)
                item['jobtag'] = ''
                for i in node['welfare']:
                    if item['jobtag'] == '':
                        item['jobtag'] = item['jobtag'] + i
                    else:
                        item['jobtag'] = item['jobtag'] + ',' + i
                item['jobtype'] = node['jobType']['display']
                item['timestate'] = node['timeState']
                item['positionurl'] = node['positionURL']
                item['updatetime'] = node['createDate']
                yield item
        except:
            print('金融岗位信息爬取完成！！')
            return
        # 智联每页90条信息，下一页域名会加90
        self.starts = self.starts + 90
        # 金融岗位网址
        new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E9%87%91%E8%9E%8D&kt=3&_v=0.24269405&x-zp-page-request-id=547349d349054a5990999a946fbdf58f-1553767441033-132396'
        # 新网址用yield返回给引擎
        yield scrapy.Request(url=new_url, callback=self.parse)
        time.sleep(2)
