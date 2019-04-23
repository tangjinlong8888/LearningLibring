# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['zhaopin.com']
    values = list(citys.values())
    print(values)
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=613&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'
                  ]

    starts = 0
    def parse(self, response):
        data = response.text
        data = json.loads(data)
        result = jsonpath.jsonpath(data, '$..results[*]')
        try:
            for node in result:
                # 实例化item对象
                item = Zhilian2Item()
                # 将岗位名称数据赋值给jobname
                item['jobname'] = node['jobName']
                item['companyname'] = node['company']['name']
                item['money'] = node['salary']
                item['city'] = node['city']['display'].split('-')[0]
                item['edulevel'] = node['eduLevel']['name']
                item['empltype'] = node['emplType']
                item['workingexp'] = node['workingExp']['name']
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
            print('爬取完成！！')
            return
        # 智联每页90条信息，下一页域名会加90
        self.starts = self.starts + 90
        for v in self.values:
            # UI岗位网址 start='+str(self.starts)+'&
            new_url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(
                self.starts) + '&pageSize=90&cityId='+v+'&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'
            time.sleep(2)
            # 新网址用yield返回给引擎
            yield scrapy.Request(url=new_url, callback=self.parse)
