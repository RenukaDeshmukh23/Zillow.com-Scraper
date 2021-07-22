# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from Zillow.utils import URL,Cookie_Parser,parse_new_url #or from .. utils import URL
from ..items import ZillowItem
import json

class RentSpider(scrapy.Spider):
    name = 'Rent'
    allowed_domains = ['zillow.com']

    def start_requests(self):
         yield scrapy.Request(
         url=URL,
         callback=self.parse,
         cookies=Cookie_Parser(),
         meta={'currentPage': 1}
         )

    def parse(self, response):
        #with open('initial_response.json','wb') as f:  Print the cookie value in dictionary format
        #    f.write(response.body)
        current_page = response.meta['currentPage']
        json_resp = json.loads(response.body)
        houses = json_resp.get('cat1').get('searchResults').get('listResults')

        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('imgSrc',house.get('imgSrc'))
            loader.add_value('address',house.get('address'))
            loader.add_value('addressZipcode',house.get('addressZipcode'))
            loader.add_value('area',house.get('area'))
            loader.add_value('baths',house.get('baths'))
            loader.add_value('beds',house.get('beds'))
            loader.add_value('brokerName',house.get('brokerName'))
            loader.add_value('detailUrl',house.get('detailUrl'))
            loader.add_value('price',house.get('price'))
            loader.add_value('statusType',house.get('statusType'))
            yield loader.load_item()

        total_pages = json_resp.get('cat1').get('searchList').get('totalPages')
        if current_page <= total_pages:
            current_page+=1
            yield scrapy.Request(
            url = parse_new_url(URL,page_number=current_page),
            callback=self.parse,
            cookies=Cookie_Parser(),
            meta={'currentPage':current_page}
            )
