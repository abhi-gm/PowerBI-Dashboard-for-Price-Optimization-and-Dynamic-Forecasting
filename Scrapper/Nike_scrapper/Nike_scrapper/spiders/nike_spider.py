import scrapy
import json 
class nike_spider(scrapy.Spider):
    name = "nike_spider"
    def start_requests(self):
        urls = [
          "https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=85689CE46EE60521D8BFBD7A686818F6&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C7baf216c-acc6-4452-9e07-39c2ca77ba32)%26anchor%3D528%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24",
          "https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=85689CE46EE60521D8BFBD7A686818F6&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C7baf216c-acc6-4452-9e07-39c2ca77ba32)%26anchor%3D504%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24",
          "https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=85689CE46EE60521D8BFBD7A686818F6&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C7baf216c-acc6-4452-9e07-39c2ca77ba32)%26anchor%3D480%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
  

    def parse(self, response):
        data = json.loads(response.text)
        for products in data['data']['products']['objects']:
            yield {
                'Product Name' : products['publishedContent']['properties']['title'] ,  
                'subtitle' : products['publishedContent']['properties']['subtitle'],
                'Full  Price' : products['productInfo'][0]['merchPrice']['fullPrice'] ,
                'Current Price'  :  products['productInfo'][0]['merchPrice']['currentPrice'],
                'Employee Price' : products['productInfo'][0]['merchPrice']['employeePrice'],
                'Image Url' :  products['publishedContent']['properties']['productCard']['properties']['squarishURL']
            }