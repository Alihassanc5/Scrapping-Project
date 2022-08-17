from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BikeSpider(CrawlSpider):
    name = 'Bike'
    allowed_domains = ['www.pakwheels.com']
    start_urls = ['https://www.pakwheels.com/used-bikes/search/-/']
    
    rules = (
        Rule(
            LinkExtractor(restrict_css='.search-title a'), callback='parse_bike', follow=False
        ),
        Rule(
            LinkExtractor(restrict_css='.next_page a'), follow=True
        )
    )

    def parse_bike(self, response):
        url = response.url
        price = response.css('.price-box strong::text').get()
        title = response.css('.well h1::text').get()
        location = response.css('.well p a::text').get()
        engine_year = response.css('.engine-icon.year + p::text').get()
        engine_millage = response.css('.engine-icon.millage + p::text').get()
        engine_type = response.css('.engine-icon.type + p::text').get()
        registered_in = response.css('.table.table-featured.nomargin td:first-child + td::text').get()
        body_type = response.css('.table.table-featured.nomargin td a::text').get()
        
        yield {
            'Url': url,
            'Price': price,
            'Title': title,
            'Location': location,
            'Engine Year': engine_year,
            'Engine Millage': engine_millage,
            'Engine Type': engine_type,
            'Registered In': registered_in,
            'Body Type': body_type,
        }
