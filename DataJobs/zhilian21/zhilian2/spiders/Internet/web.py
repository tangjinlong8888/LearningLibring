# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys

class WebSpider(scrapy.Spider):
    name = 'web'
    allowed_domains = ['zhaopin.com']
    value = list(citys.values())
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.98130800&x-zp-page-request-id=b8fb413c9a2b40498f0f6f8e7869916c-1554891324248-868570',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.05953356&x-zp-page-request-id=bf084740c1c9406ba913b716e8fc974a-1554891374561-996944',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=765&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.81861290&x-zp-page-request-id=d363088a24d5486288826c1f978f25dc-1554891438576-835012',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.41019809&x-zp-page-request-id=ec0d2f82eefc453387b2eae23d879838-1554891505262-697492',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=531&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.58666283&x-zp-page-request-id=a720990fce7647faa736d2abd2ac8be6-1554891548635-40073',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.40072646&x-zp-page-request-id=02fa1f1aae624924ba9499c8db2a070d-1554891604512-588746',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.11467536&x-zp-page-request-id=81fee0268d8a41c193ce14cb63389407-1554891633738-383200',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=736&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.64069312&x-zp-page-request-id=74fb5d75f3a942868f24a1cfb9e8033f-1554891674401-962537',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=600&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.59545988&x-zp-page-request-id=d0ce04a3842347e09e677da2434f94cc-1554891700380-908391',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=613&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.82920129&x-zp-page-request-id=d5bfc99639424c5e89d1e139188534d1-1554891783395-178368',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=635&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.59422905&x-zp-page-request-id=ae3c4bcb89fa440bbab7913d8e823774-1554891805708-104760',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.85857501&x-zp-page-request-id=096d034d504f4803bff457fc8bea1d4b-1554891828566-304170',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=703&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.61172768&x-zp-page-request-id=50140e11fdf943bca7b31ef99427808d-1554891864806-779375',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=639&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.51523120&x-zp-page-request-id=a2741855150145b1b144891464895aa8-1554891914524-719456',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=599&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.34534589&x-zp-page-request-id=158e305cfc7b4884abbee8aa38b1fa1e-1554891983666-477345',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=854&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.49689146&x-zp-page-request-id=4097a598745c4f009bf68ab4a97f9dc0-1554892006987-907417',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.11175541&x-zp-page-request-id=035c5171cce941f4a5a829bd63c8c854-1554892031154-838431',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=749&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.00022995&x-zp-page-request-id=418f4746f8e749ddbbd470ddc7ced0c7-1554892062227-860266',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=551&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.09484549&x-zp-page-request-id=0b7e3887b8e44a51a1f0be4375ae57fe-1554892113198-225964',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=622&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.32809256&x-zp-page-request-id=0ee0a81d33b2406e836d897b2a0169ad-1554892334239-785905',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=636&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.84829810&x-zp-page-request-id=84dc094773e447219ba15d18a0c4afca-1554892356433-735785',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=654&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.61902797&x-zp-page-request-id=b33c38a7c18a4a96837d884312c51f61-1554892381573-512400',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=681&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.02495315&x-zp-page-request-id=02116a375ee34e09989e6efc29df47a1-1554892438777-609665',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=682&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.51380001&x-zp-page-request-id=6eeef5401934467ea8522e99fc061dac-1554892459268-8756',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=565&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.86134457&x-zp-page-request-id=d65f1349357e428b86202e7870ac71ac-1554892479521-719590',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=664&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.61631468&x-zp-page-request-id=af8a3b6d156d4f3893491d32ddf27243-1554892551890-697967',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=773&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.75115345&x-zp-page-request-id=6d9a8e48ca764a9c9782cbbd9af66e0b-1554892570478-959604'
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
                new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId='+v+'&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Web%E5%89%8D%E7%AB%AF&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'

                # 新网址用yield返回给引擎
                yield scrapy.Request(url=new_url, callback=self.parse)


