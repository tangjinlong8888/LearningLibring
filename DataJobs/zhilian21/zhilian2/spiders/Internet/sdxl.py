# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys

class SdxlSpider(scrapy.Spider):
    name = 'sdxl'
    allowed_domains = ['zhaopin.com']
    value = list(citys.values())
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=765&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=531&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=736&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=600&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=613&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=635&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=703&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=639&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=599&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=854&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=749&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=551&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=622&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=636&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=654&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=681&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=682&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=565&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=664&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=773&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'
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
                # 将获取的字典类型的值转化成list
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
                item['city_code'] = value['code']
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
        if self.starts <= 1080:
            for v in self.value:
                # web前端岗位网址
                new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId='+v+'&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'

                # 新网址用yield返回给引擎
                yield scrapy.Request(url=new_url, callback=self.parse)


