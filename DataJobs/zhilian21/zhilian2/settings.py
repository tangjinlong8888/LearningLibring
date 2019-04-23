# -*- coding: utf-8 -*-

# Scrapy settings for zhilian2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhilian2'

SPIDER_MODULES = ['zhilian2.spiders']
NEWSPIDER_MODULE = 'zhilian2.spiders'


# 通过在用户代理上标识您自己（和您的网站）来负责地爬行
USER_AGENT = {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36',
              'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
              'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Mobile Safari/537.36',
              'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
              'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
              'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
              'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
              'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+',
              'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+',
              'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
              'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
              'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
              'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true',
              'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.132 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
              'Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
              'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',
              'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.132 Mobile Safari/537.36',
              }

# 遵守robots.txt规则
# ROBOTSTXT_OBEY = True

# 配置Scrapy执行的最大并发请求（默认值：16）
CONCURRENT_REQUESTS = 256

# 为同一网站的请求配置延迟（默认值：0）
# See https://doc.scrapy.org/en/latest/topics/settings.html#下载延迟
# 另请参见自动节流阀设置和文档
DOWNLOAD_DELAY = 2
# 下载延迟设置将仅满足以下条件之一：
CONCURRENT_REQUESTS_PER_DOMAIN = 128
CONCURRENT_REQUESTS_PER_IP = 128

# 禁用cookie（默认情况下启用）
COOKIES_ENABLED = False

# 禁用远程登录控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# 覆盖默认请求头：
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# 启用或禁用爬虫中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhilian2.middlewares.Zhilian2SpiderMiddleware': 543,
# }

# 启用或禁用下载器中间件
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'zhilian2.middlewares.Zhilian2DownloaderMiddleware': 543,
   'zhilian2.middlewares.UserAgentMiddleware':544,
   # 'zhilian2.middlewares.ProxyMiddleware':543,
}

# 启用或禁用扩展
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# 配置项目管道
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhilian2.pipelines.Zhilian2Pipeline': 300,

}

# 启用和配置自动油门扩展（默认情况下禁用）
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy平均请求数应与每个远程服务器并行发送
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示收到的每个响应的限制状态：
#AUTOTHROTTLE_DEBUG = False

# 启用和配置HTTP缓存（默认情况下禁用）
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#设置数据库配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'spider'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = '3306'

#设置cookie信息
COOKIE = {'adfbid2=0; ZP_OLD_FLAG=false; sts_deviceid=1698f8f92b969f-086f1ecd1080f1-74133f4f-1049088-1698f8f92bb959; acw_tc=2760829415528917814396051e2ed9e1cc36468bfcc444da19de6410faebb1; _jzqa=1.1534105741960119800.1552891745.1552891745.1553217255.2; _jzqy=1.1552891745.1553217255.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94.-; __xsptplus30=30.2.1553217255.1553217255.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%7C%23%23kaE4AcyhVajAN7AQyrdv8CljOUWyitlV%23; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221020362368%22%2C%22%24device_id%22%3A%221698f8f90d4269-0ae71b5b999741-74133f4f-1049088-1698f8f90d51af%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%221698f8f90d4269-0ae71b5b999741-74133f4f-1049088-1698f8f90d51af%22%7D; urlfrom2=121126445; adfcid2=none; jobRiskWarning=true; sts_sg=1; sts_chnlsid=Unknown; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1553217255,1553234148,1553267932,1553478259; dywec=95841923; __utmc=269921210; zp_src_url=https%3A%2F%2Fsou.zhaopin.com%2F%3Fjl%3D489%26sf%3D0%26st%3D0; loginreleased=1; ZPCITIESCLICKED=|801; sts_sid=169bddd3963109-020606292a4e9f-74133f4f-1049088-169bddd397818; dywea=95841923.1828852665694369800.1552891744.1553596425.1553668587.9; dywez=95841923.1553668587.9.7.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utma=269921210.2016491892.1552891745.1553596416.1553668587.8; __utmz=269921210.1553668587.8.7.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; dyweb=95841923.3.10.1553668587; __utmb=269921210.3.10.1553668587; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1553668597; sts_evtseq=7; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22ea1c08ac-dff7-4507-9a09-06bb686d16b0-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22//www%22:{%22funczone%22:%22city_hotjd%22}}; LastCity=%E6%88%90%E9%83%BD; LastCity%5Fid=801'}

#设置ip池
# IPPOOL = [
#    "http://1.196.160.137:9999","http://110.52.235.63:9999",
#    "https://218.59.193.14:47138","https://111.177.106.77	:9999","https://110.52.235.211:9999",
#    "https://117.114.149.66:53281","https://222.223.115.30:9999","https://110.52.235.219:9999",
#    "http://61.184.109.33:61320","https://221.1.200.242:38652","http://124.207.82.166:8008"
# ]