import requests
from bs4 import BeautifulSoup


class DataCollector:
    FIELD_MAPPING = (('field_name', 'value_name'), ('field', 'value'))
    PRICE_ELEMENT = '[data-cy="adPageHeaderPrice"]'
    INFORMATION_TABLE_NODES = ('area', 'terrain_area', 'building_type', 'rooms_num', 'heating_types',
                               'construction_status', 'build_year', 'car')
    VALUE_IS_HIDDEN = 'Zapytaj'

    def collect(self, url):
        data = {}
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        if self.validate_select(soup.select(self.PRICE_ELEMENT)):
            data['hash'] = hash(url)
            price_element = soup.select(self.PRICE_ELEMENT)
            data['price'] = get_price(price_element)

            for node in self.INFORMATION_TABLE_NODES:
                node_selector = '[data-testid="table-value-' + node + '"]'
                node_element = soup.select(node_selector)
                if self.validate_select(node_element):
                    node_value = node_element[0].string.replace(' m²', '')
                else:
                    node_value = None
                data[node] = node_value

        return data

    def validate_select(self, select):
        return select.__len__() > 0 and select[0].string != self.VALUE_IS_HIDDEN and select[0].string is not None


def get_price(price_element):
    price_string = price_element[0].string.replace(' ', '').replace('zł', '')
    if 'EUR' in price_string:
        price_string = price_string.replace('EUR', '')
        price_string = float(price_string) * 4.32

    return int(price_string)
