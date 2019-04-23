# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys

class PythonallSpider(scrapy.Spider):
    name = 'pythonall'
    allowed_domains = ['zhaopin.com']
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.23345555&x-zp-page-request-id=85ea2de2f89240f8accd644b20b7c1dd-1555162115321-305082'
    ]

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
                # 将岗位名称数据赋值给jobname
                item['jobname'] = node['jobName']
                item['companyname'] = node['company']['name']
                #将获取的字典类型的值转化成list
                value = node['company']['size']
                item['companysize_code'] = value['code']
                item['companysize'] = value['name']
                value = node['company']['type']
                item['companytype_code'] = value['code']
                item['companytype'] = value['name']
                value = node['workingExp']
                print(value)
                try:
                    item['workingexp_code'] = value['code']
                except:
                    item['workingexp_code'] = 0
                item['geo_lon'] = node['geo']['lon']
                item['geo_lat'] = node['geo']['lat']
                item['money'] = node['salary']
                item['city'] = node['city']['display'].split('-')[0]
                value = (node['city']['items'])[0]
                item['city_code']=value['code']
                item['edulevel'] = node['eduLevel']['name']
                item['edulevel_code'] = node['eduLevel']['code']
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
        except TypeError:
            print('爬取即将完成！！')
            return
        # 智联每页90条信息，下一页域名会加90
        self.starts = self.starts + 90
        # java开发全国岗位网址
        new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&_v=0.23345555&x-zp-page-request-id=85ea2de2f89240f8accd644b20b7c1dd-1555162115321-305082'
        # 新网址用yield返回给引擎
        yield scrapy.Request(url=new_url, callback=self.parse)


