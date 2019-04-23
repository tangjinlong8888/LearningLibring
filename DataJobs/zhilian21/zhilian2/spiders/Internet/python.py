# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys

class PythonSpider(scrapy.Spider):
    name = 'python'
    allowed_domains = ['zhaopin.com']
    value = list(citys.values())
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.37076604&x-zp-page-request-id=0f3bd2668f194362a4e176c4e9f4f8e6-1554691530516-277380',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=613&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.66988881&x-zp-page-request-id=12419a2e71394ad6a4e42c15668759d4-1554693781928-804226',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.52856939&x-zp-page-request-id=294405057fe34970b1abef03520e63e3-1554691978290-30828',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=551&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.08279234&x-zp-page-request-id=bd96f45cbce94a048ad5ddddf37527c4-1554694994048-703184',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=749&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.39148018&x-zp-page-request-id=9399eac1b30f4e519f16d5107c78dd37-1554694880063-825245',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=600&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.18109119&x-zp-page-request-id=fd60d6ea93b24aa59488d1c1f6e5ebec-1554693623934-464225',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=681&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.57891813&x-zp-page-request-id=e174c9eb99224b1bb7e0546a3f4e84d4-1554695637965-721865',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.04239710&x-zp-page-request-id=cdbb86768b634e82a75a37cc162df519-1554693018764-152549',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=664&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.06914553&x-zp-page-request-id=50c01468e3cf43ff825037a742b8f2d2-1554696061719-681245',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=622&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.76291783&x-zp-page-request-id=87a98f3da5e3474a915a36d43599a863-1554695106050-614441',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=773&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.15124612&x-zp-page-request-id=8acf2c41c3dc475f902e3ace4de25f83-1554696221764-386507',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.52568369&x-zp-page-request-id=faa1f2adda6541ce84c66905b393992e-1554693339778-377476',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.58252147&x-zp-page-request-id=ec765ec23f27462b9edf81b92826f71c-1554694050314-604050',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=654&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.60248498&x-zp-page-request-id=4227b80c1e014c25ad38de482f0fc74d-1554695331154-767116',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=635&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.05560523&x-zp-page-request-id=5541c7c47a2343fd86d3947ec33fef6f-1554693920130-740724',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=703&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.85594590&x-zp-page-request-id=f39ffb5a59814cdf87fc9d59f24696d0-1554694182617-330904',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.39257473&x-zp-page-request-id=714d396f22cd4924b4a47af89c4461d8-1554692484141-437571',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=565&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.35482584&x-zp-page-request-id=c3526440bd514259b58479667717ab76-1554695880881-620214',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=639&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.08461460&x-zp-page-request-id=b6fae2503d554d36828613b03159a6f9-1554694305706-196417',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=599&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.63427262&x-zp-page-request-id=facbd2c4d954499f965f69118fce8679-1554694464341-605974',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=765&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.21769496&x-zp-page-request-id=cdb213a1f1bf435ca086e756a362182d-1554692722118-901273',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=531&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.17434613&x-zp-page-request-id=b547601078ff467395698311f364d0bb-1554693183111-987262',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=736&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.72007031&x-zp-page-request-id=761f3d040f0242e6920d24cc9915c1d8-1554693492545-535388',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=636&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.27442110&x-zp-page-request-id=735240d105d948d982ba2f422319e8b4-1554695221566-165000',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=854&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.65860063&x-zp-page-request-id=4bb14e92a5f94e4aa8a9d17bdeae8641-1554694603226-70775',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=682&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.39979544&x-zp-page-request-id=27236ab21c5a403190d4661e40e6a787-1554695770583-879152',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.57072245&x-zp-page-request-id=a71e0fccb8bb4fd69f006fa48f0c32d1-1554694725956-666847'
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
                # python岗位网址
                new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId='+v+'&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'

                # 新网址用yield返回给引擎
                yield scrapy.Request(url=new_url, callback=self.parse)


