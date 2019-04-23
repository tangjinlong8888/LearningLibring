# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys

class JavaSpider(scrapy.Spider):
    name = 'java'
    allowed_domains = ['zhaopin.com']
    value = list(citys.values())
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.89402464&x-zp-page-request-id=9840b8700f1a47ba8ac7c50050d3bc6b-1554777501936-430712',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=613&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.70903676&x-zp-page-request-id=d3e5cc348e3d460faf2c94a94ff85fce-1554777599576-50945',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.89013876&x-zp-page-request-id=44f352489d4249c8b4d2b05d1eec187e-1554777632401-706361',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=551&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.66562916&x-zp-page-request-id=e4e41d0def9c4f6a8624b7d3a681a7cc-1554777674062-888852',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=749&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.46853269&x-zp-page-request-id=f8d612357f9a4ae2ae0c2bc9e01fc6b4-1554777711254-82899',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=600&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.52670733&x-zp-page-request-id=e7634b39654149189cb029d6bd78956e-1554777746386-866720',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=681&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.23368859&x-zp-page-request-id=6eb0f08c7346477a9635eb4971347b8b-1554777785763-4845',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.17904799&x-zp-page-request-id=ab81a2f57e4c4c3285c0af18bad0386b-1554777817699-384806',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=664&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.23257693&x-zp-page-request-id=446b280d10f848a7a371c2ba2e297677-1554777853046-625890',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=622&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.17132663&x-zp-page-request-id=3c789f60ee8f4e43813b73974f566ef3-1554777876142-994858',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=773&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.38253244&x-zp-page-request-id=6eafbdfc026344a0825f25db3e9930bd-1554777913283-486674',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.66019945&x-zp-page-request-id=f6794bd41fc14e68adc3de4c388d421b-1554777955266-873023',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.92640266&x-zp-page-request-id=4f1f4b7ac3f44644b649169d3e9640f3-1554778004337-590922',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=654&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.51729202&x-zp-page-request-id=0a5bb0d85fce4f78b0bc23b783bbbe5d-1554778043392-32070',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=635&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.25186639&x-zp-page-request-id=842702b69405405381973795884807d6-1554778078780-399763',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=703&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.83952879&x-zp-page-request-id=4c75924bbc424dc4879b2c059326c04e-1554778115613-923094',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.97530592&x-zp-page-request-id=132af9a6cc8b468ea62b480273e34628-1554777555123-519645',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=565&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.72018474&x-zp-page-request-id=31248db2f491427ea1589174087d9488-1554778148997-982382',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=639&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.41737295&x-zp-page-request-id=16a0f8e5f0224d839d3e736108278005-1554778177893-719336',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=599&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.25589713&x-zp-page-request-id=09e04e45bab14fb0b2a133c51accdb42-1554778206477-612452',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=765&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.75351743&x-zp-page-request-id=169a65e48a01461997d500375b931b39-1554778239017-41809',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=531&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.71513752&x-zp-page-request-id=778bb49e0f2b4fdba7a0f72b7baac126-1554778278329-63237',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=736&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.88432638&x-zp-page-request-id=775d46443a2e4ac2bf3c95a19a603bd9-1554778306056-938305',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=636&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.89641939&x-zp-page-request-id=13b0416fec6e4dc99773915a6507d8d8-1554778337740-782670',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=854&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.61237395&x-zp-page-request-id=0e6666a78518449cbeab5b99fef3f96f-1554778366063-135485',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=682&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.38774060&x-zp-page-request-id=32ec27bac79748b993a33c4b2f98871f-1554778400511-137964',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.21214385&x-zp-page-request-id=37dd86ad2a2e4095b6f6e4ddf095c57f-1554778434171-240989'
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
            #循环获取城市，然后在返回网址
            for v in self.value:
                # java岗位网址
                new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId='+v+'&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&rt=3b30bb5611b24ba9a62491ad552e408d'

                # 新网址用yield返回给引擎
                yield scrapy.Request(url=new_url, callback=self.parse)

