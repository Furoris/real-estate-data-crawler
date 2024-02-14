import requests
from bs4 import BeautifulSoup
from alive_progress import alive_bar


class UrlCollector:
    BASE_URL = 'https://www.otodom.pl'
    LISTING_URL = 'https://www.otodom.pl/pl/wyniki/sprzedaz/dom/cala-polska?page='
    NO_RESULT_ELEMENT = '[data-cy="no-search-results"]'

    def get_advert_urls(self, pagination_range=(1, 10)):
        urls = []
        i = pagination_range[0]
        pages = pagination_range[1] - pagination_range[0] + 1

        with alive_bar(pages, title='Processing advert urls: ') as bar:
            while i <= pagination_range[1]:
                response = requests.get(self.LISTING_URL + str(i))
                soup = BeautifulSoup(response.content, "html.parser")

                if soup.select(self.NO_RESULT_ELEMENT).__len__() > 0:
                    bar(pages)
                    print('No more results found for page ' + str(i))
                    break

                links = soup.select('[data-cy="listing-item-link"]')
                for link in links:
                    url = link.attrs['href']
                    urls.append(self.BASE_URL + url)

                bar()
                pages -= 1
                i += 1

        return urls
