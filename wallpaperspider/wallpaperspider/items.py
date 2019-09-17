# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class WallpaperspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WallpaperUrlItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()  # 图片链接
    image_paths = scrapy.Field()  # 图片保存路径
    image_names = scrapy.Field()  # 图片保存名
    image_categorys = scrapy.Field()  # 图片类别

    
class WallpaperUrlLoader(ItemLoader):
    default_item_class = WallpaperUrlItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    #description_out = Join()
