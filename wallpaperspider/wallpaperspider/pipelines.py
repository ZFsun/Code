# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from urllib.parse import urlparse
from scrapy.http import Request

class WallpaperspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class WallpaperImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_categorys = item['image_categorys']
        image_names = item['image_names']
        image_urls = item['image_urls']
        return '%s/%s' % (image_categorys, image_names) + os.path.splitext(image_urls[0])[-1]

    def get_media_requests(self, item, info):
        print('请求item:', item)
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        # print('###result###:', results)
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")

        item['image_paths'] = image_paths
        # print(item)
        return item