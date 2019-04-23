# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.conf import settings
from twisted.enterprise import adbapi
import pymysql.cursors
import socket
import urllib

#智联招聘管道
class Zhilian2Pipeline(object):

    def __init__(self):
        self.p = 0
        dbargs = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode = True,
        )
        # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbargs)
    # 默认管道调用函数
    def process_item(self, item, spider):
            self.dbpool.runInteraction(self.insert_into_table, item,spider)
            return item

    def insert_into_table(self, conn, item,spider):
        #西刺代理
        if spider.name == 'xici':
            if self.p == 0:
                conn.execute('delete from proxy_ip')
                self.p = 1
            conn.execute(
                'insert into proxy_ip(ip,port,speed,proxy_type)values(%s,%s,%s,%s)on duplicate key update ip = (ip)',
                (item['ip'], item['port'], item['speed'], item['proxy_type']))

        #智联互联网
        elif spider.name == 'zhilian_zp':
            if self.p == 0:
                conn.execute('delete from zl_computer')
                self.p = 1
            conn.execute('insert into zl_computer(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        #智联金融
        elif spider.name == 'zhilian_jr':
            if self.p == 0:
                conn.execute('delete from zl_jinrong')
                self.p = 1
            conn.execute(
                'insert into zl_jinrong(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'],item['companysize_code'],item['companytype'],item['companytype_code'],item['edulevel'],
                 item['empltype'], item['jobname'],item['jobtag'], item['jobtype'],item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'],item['workingexp_code'],item['geo_lon'],item['geo_lat']))
        #智联房地产
        elif spider.name == 'zhilian_fdc':
            if self.p == 0:
                conn.execute('delete from zl_fangdc')
                self.p = 1
            conn.execute(
                'insert into zl_fangdc(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'], item['companysize_code'], item['companytype'],
                 item['companytype_code'], item['edulevel'],
                 item['empltype'], item['jobname'], item['jobtag'], item['jobtype'], item['money'], item['positionurl'],
                 item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        #智联零售/贸易/物流
        elif spider.name == 'zhilian_wl':
            if self.p == 0:
                conn.execute('delete from zl_wuliu')
                self.p = 1
            conn.execute(
                'insert into zl_wuliu(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'],item['companysize_code'],item['companytype'],item['companytype_code'],item['edulevel'],
                 item['empltype'], item['jobname'],item['jobtag'], item['jobtype'],item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'],item['workingexp_code'],item['geo_lon'],item['geo_lat']))
        #智联教育
        elif spider.name == 'zhilian_jy':
            if self.p == 0:
                conn.execute('delete from zl_jiaoyu')
                self.p = 1
            conn.execute(
                'insert into zl_jiaoyu(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'], item['companysize_code'], item['companytype'],
                 item['companytype_code'], item['edulevel'],
                 item['empltype'], item['jobname'], item['jobtag'], item['jobtype'], item['money'], item['positionurl'],
                 item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        #智联服务业
        elif spider.name == 'zhilian_fw':
            if self.p == 0:
                conn.execute('delete from zl_fuwu')
                self.p = 1
            conn.execute(
                'insert into zl_fuwu(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'], item['companysize_code'], item['companytype'],
                 item['companytype_code'], item['edulevel'],
                 item['empltype'], item['jobname'], item['jobtag'], item['jobtype'], item['money'], item['positionurl'],
                 item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        #智联市场/销售
        elif spider.name == 'zhilian_xs':
            if self.p == 0:
                conn.execute('delete from zl_xiaoshou')
                self.p = 1
            conn.execute(
                'insert into zl_xiaoshou(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'],item['companysize_code'],item['companytype'],item['companytype_code'],item['edulevel'],
                 item['empltype'], item['jobname'],item['jobtag'], item['jobtype'],item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'],item['workingexp_code'],item['geo_lon'],item['geo_lat']))
        #智联人事/行政/前台
        elif spider.name == 'zhilian_xz':
            if self.p == 0:
                conn.execute('delete from zl_xingzheng')
                self.p = 1
            conn.execute(
                'insert into zl_xingzheng(city,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['companyname'], item['companysize'], item['companysize_code'], item['companytype'],
                 item['companytype_code'], item['edulevel'],
                 item['empltype'], item['jobname'], item['jobtag'], item['jobtype'], item['money'], item['positionurl'],
                 item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # python岗位
        elif spider.name == 'python':
            if self.p == 0:
                conn.execute('delete from python')
                self.p = 1
            conn.execute(
                'insert into python(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'],item['companyname'], item['companysize'],item['companysize_code'],item['companytype'],item['companytype_code'],item['edulevel'],
                 item['edulevel_code'],item['empltype'], item['jobname'],item['jobtag'], item['jobtype'],item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'],item['workingexp_code'],item['geo_lon'],item['geo_lat']))
        # java岗位
        elif spider.name == 'java':
            if self.p == 0:
                conn.execute('delete from java')
                self.p = 1
            conn.execute(
                'insert into java(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        #UI设计师岗位
        elif spider.name == 'UI':
            if self.p == 0:
                conn.execute('delete from UI')
                self.p = 1
            conn.execute(
                'insert into UI(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        #web前端岗位
        elif spider.name == 'web':
            if self.p == 0:
                conn.execute('delete from web')
                self.p = 1
            conn.execute(
                'insert into web(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # PHP岗位
        elif spider.name == 'php':
            if self.p == 0:
                conn.execute('delete from php')
                self.p = 1
            conn.execute(
                'insert into php(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # android岗位
        elif spider.name == 'android':
            if self.p == 0:
                conn.execute('delete from android')
                self.p = 1
            conn.execute(
                'insert into android(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 美工岗位
        elif spider.name == 'meigong':
            if self.p == 0:
                conn.execute('delete from meigong')
                self.p = 1
            conn.execute(
                'insert into meigong(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 深度学习岗位
        elif spider.name == 'sdxl':
            if self.p == 0:
                conn.execute('delete from sdxl')
                self.p = 1
            conn.execute(
                'insert into sdxl(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 算法工程师岗位
        elif spider.name == 'suanfagcs':
            if self.p == 0:
                conn.execute('delete from suanfagcs')
                self.p = 1
            conn.execute(
                'insert into suanfagcs(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 全国web前端岗位
        elif spider.name == 'weball':
            if self.p == 0:
                conn.execute('delete from weball')
                self.p = 1
            conn.execute(
                'insert into weball(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 全国java开发岗位
        elif spider.name == 'javaall':
            if self.p == 0:
                conn.execute('delete from javaall')
                self.p = 1
            conn.execute(
                'insert into javaall(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 全国java开发岗位
        elif spider.name == 'pythonall':
            if self.p == 0:
                conn.execute('delete from pythonall')
                self.p = 1
            conn.execute(
                'insert into pythonall(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 全国php开发岗位
        elif spider.name == 'phpall':
            if self.p == 0:
                conn.execute('delete from phpall')
                self.p = 1
            conn.execute(
                'insert into phpall(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 全国php开发岗位
        elif spider.name == 'uiall':
            if self.p == 0:
                conn.execute('delete from uiall')
                self.p = 1
            conn.execute(
                'insert into uiall(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
        # 全国php开发岗位
        elif spider.name == 'androidall':
            if self.p == 0:
                conn.execute('delete from androidall')
                self.p = 1
            conn.execute(
                'insert into androidall(city,city_code,companyname,companysize,companysize_code,companytype,companytype_code,edulevel,edulevel_code,empltype,jobname,jobtag,jobtype,money,positionurl,updatetime,timestate,workingexp,workingexp_code,geo_lon,geo_lat)'
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)on duplicate key update jobname = (jobname), companyname = (companyname)',
                (item['city'], item['city_code'], item['companyname'], item['companysize'], item['companysize_code'],
                 item['companytype'], item['companytype_code'], item['edulevel'],
                 item['edulevel_code'], item['empltype'], item['jobname'], item['jobtag'], item['jobtype'],
                 item['money'], item['positionurl'], item['updatetime'], item['timestate'],
                 item['workingexp'], item['workingexp_code'], item['geo_lon'], item['geo_lat']))
