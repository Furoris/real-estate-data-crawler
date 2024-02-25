from url_collector import UrlCollector
from data_collector import DataCollector
from data_saver import DataSaver
from alive_progress import alive_bar
import time

STARTING_PAGE = 1
ENDING_PAGE = 20

url_collector = UrlCollector()
data_collector = DataCollector()
advert_urls = url_collector.get_advert_urls((STARTING_PAGE, ENDING_PAGE))

rows = []
with alive_bar(advert_urls.__len__(), title='Processing adverts data: ') as bar:
    for advert_url in advert_urls:
        rows.append(data_collector.collect(advert_url))
        if rows.__len__() % 5 == 0:
            time.sleep(3)  # sleep 3 second every 5 pages processed
        bar()

saver = DataSaver()
saver.save_advert_data(rows)

print('Data preparation done.')
