from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.join(os.getcwd()))
crawlline = 'xici'
execute(['scrapy','crawl',crawlline])

