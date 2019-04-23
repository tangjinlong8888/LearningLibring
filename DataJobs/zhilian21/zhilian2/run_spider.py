from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from zhilian2.spiders.Internet.zhilian_zp import ZhilianZpSpider
from zhilian2.spiders.zhilian_fdc import ZhilianFdcSpider
from zhilian2.spiders.zhilian_fw import ZhilianFwSpider
from zhilian2.spiders.zhilian_jr import ZhilianJrSpider
from zhilian2.spiders.zhilian_jy import ZhilianJySpider
from zhilian2.spiders.zhilian_wl import ZhilianWlSpider
from zhilian2.spiders.zhilian_xs import ZhilianXsSpider
from zhilian2.spiders.zhilian_xz import ZhilianXzSpider

#导入python爬虫
from zhilian2.spiders.Internet.python import PythonSpider
#导入java爬虫
from zhilian2.spiders.Internet.java import JavaSpider
#导入UI爬虫
from zhilian2.spiders.Internet.UI import UiSpider
#导入web前端爬虫
from zhilian2.spiders.Internet.web import WebSpider
from zhilian2.spiders.Internet.php import PhpSpider
from zhilian2.spiders.Internet.android import AndroidSpider
from zhilian2.spiders.Internet.meigong import MeigongSpider
from zhilian2.spiders.Internet.sdxl import SdxlSpider
from zhilian2.spiders.Internet.suanfagcs import SuanfagcsSpider
from zhilian2.spiders.Internet.web_all import WeballSpider
from zhilian2.spiders.Internet.java_all import JavaallSpider
from zhilian2.spiders.Internet.python_all import PythonallSpider
from zhilian2.spiders.Internet.phpall import PhpallSpider
from zhilian2.spiders.Internet.uiall import UIallSpider
from zhilian2.spiders.Internet.androidall import AndroidallSpider
import logging

logging = logging.getLogger(__name__)

setting = get_project_settings()
configure_logging(setting)
runner = CrawlerRunner(setting)

#装载爬虫
def start_spider():


    # #智联八大岗位
    # runner.crawl(ZhilianXsSpider)
    # runner.crawl(ZhilianXzSpider)
    # runner.crawl(ZhilianZpSpider)
    # runner.crawl(ZhilianJrSpider)
    # runner.crawl(ZhilianFdcSpider)
    # runner.crawl(ZhilianFwSpider)
    # runner.crawl(ZhilianJySpider)
    # runner.crawl(ZhilianWlSpider)

    # #智联招聘python岗位主要城市
    # runner.crawl(PythonSpider)
    # #智联招聘java岗位主要城市
    # runner.crawl(JavaSpider)
    # #智联招聘UI岗位主要城市
    # runner.crawl(UiSpider)
    # #智联招聘web前端岗位主要城市
    # runner.crawl(WebSpider)
    # #智联招聘PHP岗位
    # runner.crawl(PhpSpider)
    # #智联招聘Android岗位
    # runner.crawl(AndroidSpider)
    # #智联招聘美工岗位
    # runner.crawl(MeigongSpider)
    #智联招聘深度学习岗位
    runner.crawl(SdxlSpider)
    # #算法工程师岗位
    # runner.crawl(SuanfagcsSpider)

    #全国岗位
    # runner.crawl(WeballSpider)
    # runner.crawl(JavaallSpider)
    # runner.crawl(PythonallSpider)
    # runner.crawl(PhpallSpider)
    # runner.crawl(UIallSpider)
    # runner.crawl(AndroidallSpider)
    #爬虫结束后停止事件循环
    d = runner.join()
    d.addBoth(lambda _:reactor.stop())

    #启动事件循环
    reactor.run()

def main():
    start_spider()

if __name__ == '__main__':
    main()
