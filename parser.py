import requests
import datetime
import urllib

DOMAIN = 'http://www.pogoda.by/news/index.php'

def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise HTTPError(response.status_code)


def create_pogoda_news_urls_list(date_from, years_deep):
    months_deep = years_deep*12;

    for month in range(months_deep+1):
        date = date_from - datetime.timedelta(month=month)
        month = date.month
        year = date.year




if __name__ == '__main__':
    print(get_url(DOMAIN))

