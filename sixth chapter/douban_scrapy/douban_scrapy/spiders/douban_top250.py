import scrapy

from scrapy import Request
from typing import Iterable
from ..items import DoubanScrapyItem


class DoubanTop250Spider(scrapy.Spider):
    name = "douban_top250"
    allowed_domains = ["movie.douban.com"]

    # 可以在这里设置cookie
    # cookie = {'User-Agent': '',}  # 可以加在Request的参数中
    # start_urls = ["https://movie.douban.com"]

    # 如果需要爬取分页的页面，那么需要在这里面
    def start_requests(self) -> Iterable[Request]:
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, response, **kwargs):
        item = DoubanScrapyItem()
        # 如果想要请求更加具体的页面, 在这里发出更加具体的请求
        page_detail = response.xpath('')
        for page in page_detail:
            detail_a = page.xpath('').extrach_first()
            yield Request(url=detail_a, callback=self.parse_detail, method='GET', cb_kwargs={'item': item})

    def parse_detail(self, response, **kwargs):
        # 在这里进行提取数据，用item来封装
        item = kwargs['item']
        # 提取详细页的内容
        intro = response.xpath('').extract_first()
        date = response.xpath('').extract_first()

        item['intro'] = intro
        item['date'] = date

        yield item

