# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #id = scrapy.Field()
    imgSrc = scrapy.Field()
    statusType = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    beds = scrapy.Field()
    baths = scrapy.Field()
    detailUrl = scrapy.Field()
    addressZipcode = scrapy.Field()
    area = scrapy.Field()
    brokerName = scrapy.Field()
