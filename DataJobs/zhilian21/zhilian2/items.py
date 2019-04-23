# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#西刺代理
class XiciItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    speed = scrapy.Field()
    proxy_type = scrapy.Field()

#智联招聘
class Zhilian2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    companyname = scrapy.Field()
    companysize = scrapy.Field()
    companysize_code = scrapy.Field()
    companytype = scrapy.Field()
    companytype_code = scrapy.Field()
    money = scrapy.Field()
    city = scrapy.Field()
    city_code = scrapy.Field()
    edulevel = scrapy.Field()
    edulevel_code = scrapy.Field()
    empltype = scrapy.Field()
    workingexp = scrapy.Field()
    workingexp_code = scrapy.Field()
    jobtag = scrapy.Field()
    jobtype = scrapy.Field()
    timestate = scrapy.Field()
    positionurl = scrapy.Field()
    updatetime = scrapy.Field()
    geo_lon = scrapy.Field()
    geo_lat = scrapy.Field()

