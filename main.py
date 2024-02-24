from url_collector import UrlCollector
from data_collector import DataCollector

url_collector = UrlCollector()
data_collector = DataCollector()
advert_urls = url_collector.get_advert_urls((1, 1))

for advert_url in advert_urls:
    row = data_collector.collect(advert_url)

print('Data preparation done.')
