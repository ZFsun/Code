# -*- coding: utf-8 -*-
import scrapy
from wallpaperspider.items import WallpaperUrlItem

class Win4000Spider(scrapy.Spider):
    name = 'win4000'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/zt/youxi_4.html']

    def parse(self, response):

        try:
            next_url = response.xpath("//a[@class='next']/@href")[0].root
            print('next_url', next_url)
            yield scrapy.Request(next_url, callback=self.parse)
        except IndexError:
            next_url = ''

        detail_page_url = response.xpath("//div[@class='Left_bar']//ul[@class='clearfix']//li//a/@href")
        for detail_url in detail_page_url:
            # print('detail_url:', detail_url.root)
            yield scrapy.Request(detail_url.root, callback=self.detail_page)

    def detail_page(self, response):
        item = WallpaperUrlItem()
        image_imgs_selector = response.xpath("//div[@class='col-main']/div[@class='main-wrap']//img[@class='pic-large']")
        print(image_imgs_selector)
        print(image_imgs_selector.xpath("/@src"))
        image_urls_ = image_imgs_selector.attrib['src']
        image_names = image_imgs_selector.attrib['title']

        image_urls = []
        image_urls.append(image_urls_)
        item['image_urls'] = image_urls
        item['image_names'] = image_names
        item['image_categorys'] = '游戏'
        # print('item:', item)
        yield item
