import requests
from requests.models import PreparedRequest
import datetime
import dateutil.relativedelta
from bs4 import BeautifulSoup
import re


DOMAIN = 'http://www.pogoda.by/news/index.php'

MONTHS= {
    1 : "Января",
    2 : "Февраля",
    3 : "Марта",
    4 : "Апреля",
    5 : "Мая",
    6 : "Июня",
    7 : "Июля",
    8 : "Августа",
    9 : "Сентября",
    10 : "Октября",
    11 : "Ноября",
    12 :"Декабря"
}

def get_url(url):

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise requests.HTTPError(response.status_code)

def add_start_zero(month):
    m = int(month)
    if m < 10:
       return '0'+str(month)
    return month 


def create_pogoda_news_urls_list(date_from, years_deep):
    months_deep = years_deep*12;
    urls_list = []
    for month in range(months_deep+1):
        date = date_from - dateutil.relativedelta.relativedelta(months=month)
        month = add_start_zero(date.month)
        year = date.year
        params = {'month': month, 'year':year}
        req = PreparedRequest()
        req.prepare_url(DOMAIN, params)
        urls_list.append(req.url)
    return urls_list

def find_text_in_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', {"id": "content"})
    p_list = soup.findAll('p')
    p_no_tags_list = []
    tag = re.compile('<.*?>')
    for item in p_list:
        for child in item.children:
            if not re.search(tag, str(child)):
                p_no_tags_list.append(str(child))
    return p_no_tags_list

def find_month_in_text(text):
    for k,v in MONTHS.items():
        if type(text) == str:
            clear_text = text.replace("\r\n","")
            r = re.search(v, clear_text)
            if r:    
                return {'text': clear_text, 'month': k, 'start': r.start()}
            r = re.search(v.lower(), clear_text)
            if r:    
                return {'text': clear_text, 'month': k, 'start': r.start()}
    return None

def month_find_list(tex_list):
    l =[]
    for item in tex_list:
        d = find_month_in_text(item)
        if d:
            l.append(d)
    return l

def find_day_in_text(month_dict_list):
    digits = re.compile('') 
    for item in month_dict_list:
        string = item['text'][0:item['start']]
        


if __name__ == '__main__':
    urls = create_pogoda_news_urls_list(datetime.datetime.now(), 1)
    html = get_url(urls[0])
    text_list = find_text_in_html(html)
    month_list = month_find_list(text_list)
    find_day_in_text(month_list)

