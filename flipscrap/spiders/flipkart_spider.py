import scrapy


class FlipkartSpider(scrapy.Spider):
    name = "flipkart"

    def start_requests(self):
        urls = [
            'https://www.flipkart.com/realme-2-pro-blue-ocean-64-gb/p/itmf944x6fh8uzjy?pid=MOBF944XVM3EMXTV&srno=b_1_1&otracker=hp_omu_Mobile%2BNew%2BLaunches_5_16MP%252B2MP%2B%257C16MP%2BCamera_JD4HDS1J0RUD_4&lid=LSTMOBF944XVM3EMXTVV5USVO&fm=neo%2Fmerchandising&iid=20289778-ed40-4e53-b00a-45690915aa1c.MOBF944XVM3EMXTV.SEARCH&ppt=Homepage&ppn=Homepage&ssid=u3c0mrzb740000001544346871852',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield{
            'price': response.xpath("//div[@class='_1vC4OE _3qQ9m1']//text()").extract()
        }
        