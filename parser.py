import requests
from requests.models import PreparedRequest
import datetime
import dateutil.relativedelta

DOMAIN = 'http://www.pogoda.by/news/index.php'

def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise requests.HTTPError(response.status_code)


def create_pogoda_news_urls_list(date_from, years_deep):
    months_deep = years_deep*12;
    urls_list = []
    for month in range(months_deep+1):
        date = date_from - dateutil.relativedelta.relativedelta(months=month)
        month = date.month
        year = date.year
        params = {'month': month, 'year':year}
        req = PreparedRequest()
        req.prepare_url(DOMAIN, params)
        urls_list.append(req.url)

if __name__ == '__main__':
    create_pogoda_news_urls_list(datetime.datetime.now(), 1)

