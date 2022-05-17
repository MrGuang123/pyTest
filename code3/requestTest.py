from cmath import log
import requests
import logging
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'


def scrape_api(url):
    logging.info('scraping %s--', url)
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            return response.json()
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except:
        logging.error('error occurred while scraping %s', url, exc_info=True)


LIMIT = 10


def scrape_index(index):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (index - 1))
    return scrape_api(url)


DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


TOTAL_PAGE = 10

result = []


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for inx, item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)


if __name__ == '__main__':
    main()
