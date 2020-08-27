import requests
from requests.models import PreparedRequest
import datetime
import dateutil.relativedelta
from bs4 import BeautifulSoup
import re
import csv
import nltk
from nltk.corpus import stopwords
import rulemma

DOMAIN = 'http://www.pogoda.by/news/index.php'

MONTHS_GEN = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}

MONTH_LIST = ['январь', "февраль", "март", "апрель",
            "май", "июнь", "июль", "август",
            "сентябрь", "октябрь", "ноябрь", "декабрь"
            ]

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
    for k,v in MONTHS_GEN.items():
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
    result = []
    digits = re.compile('\d+')
    digits_defis = re.compile('\d+-\d+') 
    for index, item in enumerate(month_dict_list):
        text = item['text'][0:item['start']]
        match_digit = re.search(digits, text)
        match_digits_defis = re.search(digits_defis, text)
        if match_digits_defis:
           days = []
           days_str = re.split('-',match_digits_defis.group(0))
           for day in days_str:
                days.append(int(day))
           text = item['text'].lstrip(' ')
           result.append({'text': text, 'month': item['month'], 'days':days})
        elif match_digit:
           days = [int(match_digit.group(0))]
           text = item['text'].lstrip(' ')
           result.append({'text': text, 'month': item['month'], 'days':days})
    return result


def list_to_scv(list, path):
   
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["test", "month", "days"])
        for item in list:
            writer.writerow([item['text'], item['month'], item['days']])

def clear_words(words):
    # lemmatizer = rulemma.Lemmatizer()
    # lemmatizer.load()
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на','см',
                       '...', '..', ',', '.', 'м/с', 'В', '(', ')', ':', '-', '–', ';', '!'])
    cleared = []
    for word in words:
        if word.lower() not in stop_words:
            if not re.search('°', word)\
                    and not re.match(r'^[-\+]\d+', word):
                # lemma = lemmatizer.get_lemma(word.lower())
                # if type(lemma) == tuple:
                #     cleared.append(lemma[0])
                # elif type(lemma) == str:
                    cleared.append(word.lower())

    return cleared



def is_month_and_date_in_tokens(tokens):
    is_month = False
    is_digit = False
    for token in tokens:
        if token in MONTH_LIST:
            is_month = True
        if token.isnumeric():
            is_digit = True

    return is_month and is_digit


def count_words_in_list(word, list):
    count = 0
    for i in list:
        if word == i:
            count += 1
    return count


if __name__ == '__main__':
    cleared_tuple = set()
    # urls = create_pogoda_news_urls_list(datetime.datetime.now(), 10)
    # weather_list = []
    # for url in urls:
    #     html = get_url(url)
    #     text_list = find_text_in_html(html)
    #     month_list = month_find_list(text_list)
    #     days = find_day_in_text(month_list)
    #     weather_list.extend(days)
    # list_to_scv(weather_list, 'weather_forecast.csv')
    #     with open('weather_tokens.csv', 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["tokens", "month", "days"])
    #         for row in reader:
    #             i += 1
    #             text = row['text']
    #             month = row['month']
    #             days = row['days']
    #             print(i)
    #             sentences = nltk.sent_tokenize(text)
    #             for sentence in sentences:
    #                 words = nltk.word_tokenize(sentence)
    #                 # words = clear_words(words)
    #                 # if is_month_and_date_in_tokens(words):
    #                 writer.writerow([words, month, days])

    # bag = set()
    # months = list(MONTHS_GEN.values())
    # digits_defis = re.compile('\d+-\d+')
    # with open('weather_forecast.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         text = row['text']
    #         sentences = nltk.sent_tokenize(text)
    #         for sentence in sentences:
    #             words = nltk.word_tokenize(sentence)
    #             cleared_words = clear_words(words)
    #             print(cleared_words)
    #             for index, word in enumerate(cleared_words):
    #                 if word in months:
    #                     bag.add(word)
    #                     print(word)
    #                     if index > 0:
    #                         prev_word = cleared_words[index-1]
    #                         if re.match(digits_defis, prev_word):
    #                             bag.add(prev_word)
    #
    # for index, i in enumerate(range(1, 32)):
    #     bag.add(str(i))
    #     if i < 31:
    #         bag.add(str(i)+'-'+str(i+1))
    #
    # for item in bag:
    #     print(item)
    # with open('words_bag.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["bag"])
    #     for word in bag:
    #         writer.writerow([word])

    bag = set()
    d_list = []
    with open('words_bag.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = row['bag']
            bag.add(str(item))

    with open('weather_forecast.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            text = row['text']
            month = row['month']
            days = row['days']
            days = days.replace('[', '')
            days = days.replace(']', '')
            days = days.replace(' ', '')
            day_list = days.split(',')
            words = nltk.word_tokenize(text)
            cleared_words = clear_words(words)
            d = {}
            d['text'] = text
            for item in bag:
                d[item] = count_words_in_list(item, words)
            d['month'] = month
            d['day_start'] = day_list[0]
            if len(day_list) > 1:
                d['day_end'] = day_list[1]
            else:
                d['day_end'] = day_list[0]
            d_list.append(d)
    with open('weather_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(k for k, v in d_list[0].items())
        for d in d_list:
            writer.writerow(v for k, v in d.items())



    # i = 0
    # with open('weather_tokens.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     with open('weather_cleared.csv', 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["tokens", "month", "days"])
    #         for row in reader:
    #             i += 1
    #             words = row['tokens']
    #             month = row['month']
    #             days = row['days']
    #             print(i)
    #             words = clear_words(words)
    #             if is_month_and_date_in_tokens(words):
    #                 writer.writerow([words, month, days])