from url_collector import UrlCollector
from data_collector import DataCollector
from data_saver import DataSaver
from alive_progress import alive_bar

url_collector = UrlCollector()
data_collector = DataCollector()
advert_urls = url_collector.get_advert_urls((1, 1))

rows = []
with alive_bar(advert_urls.__len__(), title='Processing adverts data: ') as bar:
    for advert_url in advert_urls:
        rows.append(data_collector.collect(advert_url))
        bar()

saver = DataSaver()
saver.save_advert_data(rows)

print('Data preparation done.')
