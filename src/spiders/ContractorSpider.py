import scrapy
import json
from items.ContractorItem import ContractorItem


class ContractorSpider(scrapy.Spider):
    name = 'contractor'

    def start_requests(self):
        yield scrapy.Request(url='https://www.buildzoom.com/contractor/homes-by-carousel-inc', callback=self.parse, meta={'proxy': 'http://192.168.11.82:9966'})
    
    def correctStr(self, str):
        if str is None:
            return ""
        else:
            return str

    def parse(self, response):
        data = response.xpath("//div[@id='new-review']/a/@contractor").get()
        data = json.loads(data)
        #
        # name
        name = data['business_name']
        #
        # url
        url = response.url
        #
        # description
        description = response.xpath(
            "//meta[@name='description']/@content").get()
        #
        # category
        category = data['schema_type']
        #
        # rating
        rating = response.xpath(
            '//div[@itemprop="aggregateRating"]/a/@title').get()
        if not (rating is None):
            rating = float(rating.split(' ')[0])
        #
        # rating_buildzoom
        rating_buildzoom = data['score']
        #
        # phone
        phone = str(response.xpath(
            '//div[@itemprop="telephone"]/a/text()').get()).strip()
        #
        # email
        email = data['email']
        #
        # website
        website = data['website']
        #
        # is_licensed
        is_licensed = data['licensed']
        #
        # license_info
        license_info = data['license']
        #
        # insured_value
        insured_value = data['insured_amount']
        if insured_value == '':
            insured_value = None
        #
        # bond_value
        bond_value = data['bonded_amount']
        if bond_value == '':
            bond_value = None
        #
        # street_address
        street_address = data['street_address']
        #
        # city
        city = data['city']
        #
        # state
        state = data['state']
        #
        # zipcode
        zipcode = data['zipcode']
        #
        # full_address
        full_address = self.correctStr(street_address) + " " + self.correctStr(city) + " " + self.correctStr(state) + " " + self.correctStr(zipcode)
        full_address = full_address.strip()
        #
        # image
        image = response.xpath("//div[@id='gallery']//img/@src").get()
        if not (image is None):
            image = 'http:' + str(image)
        else:
            image = ''
        #
        # updated_at
        info_updated_at = data['work_preferences']['updated_at']
        #
        # employee
        employee = {}
        for elem in response.xpath("//div[@itemprop='employee']/div[@class='employee-description']"):
            employee[elem.xpath(".//div[@itemprop='name']/text()").get()
                     ] = elem.xpath(".//div[@itemprop='jobTitle']/text()").get()
        #
        # work_preferences
        work_preferences = data['work_preferences']

        yield ContractorItem(**{
            'name': name,
            'url': url,
            'description': description,
            'category': category,
            'rating': rating,
            'rating_buildzoom': rating_buildzoom,
            'phone': phone,
            'email': email,
            'website': website,
            'is_licensed': is_licensed,
            'license_info': license_info,
            'insured_value': insured_value,
            'bond_value': bond_value,
            'street_address': street_address,
            'city': city,
            'state': state,
            'zipcode': zipcode,
            'full_address': full_address,
            'image_urls': [image],
            'info_updated_at': info_updated_at,
            'employee': employee,
            'work_preferences': work_preferences,
        })
