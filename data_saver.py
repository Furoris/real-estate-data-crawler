import pandas as pd
import os.path


class DataSaver:
    SAVE_LOCATION = 'data/'
    ADVERT_URLS_FILE = 'advert_urls.csv'
    ADVERT_DATA_FILE = 'advert_data.csv'

    def save_advert_urls(self, urls):
        urls += self.open_advert_urls()
        header = ['url']
        df = pd.DataFrame(urls, columns=header)
        df = df.drop_duplicates(keep='first')
        df.to_csv(self.SAVE_LOCATION + self.ADVERT_URLS_FILE, index=False)

    def open_advert_urls(self):
        urls = []
        path = self.SAVE_LOCATION + self.ADVERT_URLS_FILE
        check_file = os.path.isfile(path)

        if check_file:
            urls = pd.read_csv(path)
            urls = urls['url'].tolist()

        return urls

    def save_advert_data(self, data):
        data += self.open_advert_data()
        df = pd.DataFrame.from_dict(data)
        df = df.drop_duplicates(['hash'], keep='first')
        df.to_csv(self.SAVE_LOCATION + self.ADVERT_DATA_FILE, index=False)

    def open_advert_data(self):
        data = []
        path = self.SAVE_LOCATION + self.ADVERT_DATA_FILE
        check_file = os.path.isfile(path)

        if check_file:
            data = pd.read_csv(path)

        return data
