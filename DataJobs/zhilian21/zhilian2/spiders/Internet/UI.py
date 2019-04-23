# -*- coding: utf-8 -*-
import scrapy
from zhilian2.items import Zhilian2Item
import json
import jsonpath
import time
from zhilian2.citys import citys

class UiSpider(scrapy.Spider):
    name = 'UI'
    allowed_domains = ['zhaopin.com']
    value = list(citys.values())
    #开始地址
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.68496062&x-zp-page-request-id=21db284347ec487bb2bd97d71e8b0b8f-1554779812973-749385',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=613&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.87661937&x-zp-page-request-id=87e62661323d4f31afabf59cd0215c14-1554780061451-845259',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.36265871&x-zp-page-request-id=6a74db68a9cf4eb893d9a4743c492d9b-1554780112162-450631',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=551&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.79914880&x-zp-page-request-id=952abc1245f147f4a0e88fc9428231c0-1554780172552-842480',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=749&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.10015126&x-zp-page-request-id=c2be8ca6e9ce487ab1a5e12782637125-1554780233934-436421',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=600&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.68927049&x-zp-page-request-id=ea50ec18080b409aad5d6ff3a8d04427-1554780298232-453476',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=681&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.53041816&x-zp-page-request-id=c0f89ad789614f1bbc9cc4ffd4a239b2-1554780368795-269032',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.04982315&x-zp-page-request-id=e3c26ecc12024a61afc79f9ac83d60f8-1554780691759-545824',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=664&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.49789434&x-zp-page-request-id=8d56b9234d334316853478bbf4b90e83-1554780778067-797623',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=622&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.87930638&x-zp-page-request-id=6a064109b8294ca9aea4812b2c39a3b3-1554781584019-840044',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=773&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.09956800&x-zp-page-request-id=634b461a8c13480587d68c718c43c17b-1554781663442-955723',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.20889657&x-zp-page-request-id=f40b7283b34c4c5d9a01b1ef854b7f1d-1554781728180-739741',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.33810258&x-zp-page-request-id=13a8a2418b7f4dabaeec813641e31172-1554784107308-968554',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=654&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.36396412&x-zp-page-request-id=18a4ebf80e014d46bdb6b78700bda446-1554784174484-993632',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=635&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.08986426&x-zp-page-request-id=93dfe57798ea40389bd36c04759fd448-1554784229165-421327',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=703&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.98528223&x-zp-page-request-id=913ee707505943e9a90786dd1ad15406-1554784281885-649305',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.77335630&x-zp-page-request-id=53ad280a538440718b54228847d0bd61-1554784377273-669854',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=565&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.55324426&x-zp-page-request-id=a49460bed2174a69bed99e2d6e7a623f-1554784428602-350347',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=639&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.86277217&x-zp-page-request-id=806dbe13b9a14aafaeb200e37e7e6ffe-1554784493035-219468',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=599&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.34672622&x-zp-page-request-id=3eaabfc23e03433ebca8da49db663a12-1554784546092-289739',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=765&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.10418598&x-zp-page-request-id=4cbf18cfc7374ac7aa2f5b9acc8be9b3-1554784603099-175919',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=531&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.64652053&x-zp-page-request-id=f83e1b0595684e1b9bd53ce1fa9e0b90-1554864392417-684126',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=736&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.42425856&x-zp-page-request-id=67a4d94c00d34d95ae47c3c0ef4fe78d-1554785626592-421653',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=636&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.19077044&x-zp-page-request-id=0cd1b4aa9dbf46b1907009ebeae56f42-1554785715083-962270',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=854&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.22287532&x-zp-page-request-id=014e02030aaa4e1a8af7eb245d196a72-1554785762894-649945',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=682&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.53971433&x-zp-page-request-id=8a60f21b242b4bd4a03117a91f63efbf-1554785811384-236094',
                  'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d&_v=0.50402838&x-zp-page-request-id=e142f33ab2d845198e7636d0a5ad85ea-1554785864308-165177'
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
                # UI岗位网址
                new_url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(self.starts)+'&pageSize=90&cityId='+v+'&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&=0&rt=3b30bb5611b24ba9a62491ad552e408d'

                # 新网址用yield返回给引擎
                yield scrapy.Request(url=new_url, callback=self.parse)


