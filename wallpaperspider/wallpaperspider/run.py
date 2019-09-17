# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 22:01
# @Author  : ZPF
# @Email   : 499428970@qq.com
# @File    : run.py
# @Software: PyCharm

from scrapy import cmdline
from wallpaperspider.spiders import win4000
from scrapy.crawler import CrawlerProcess

# cmdline.execute('scrapy crawl win4000'.split(' '))

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(win4000)
process.start() # the script will block here until the crawling is finished