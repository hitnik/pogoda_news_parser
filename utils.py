import re
import csv
import nltk
from nltk.corpus import stopwords


def clear_words(words):
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на','см',
                       '...', '..', ',', '.', 'м/с', 'В', '(', ')', ':', '-', '–', ';', '!'])
    cleared = []
    for word in words:
        if word.lower() not in stop_words:
            if not re.search('°', word)\
                    and not re.match(r'^[-\+]\d+', word):
                    cleared.append(word.lower())

    return cleared

def sentence_to_bagofwords(sentence):
    bag = set()
    d_list = []
    with open('words_bag.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = row['bag']
            bag.add(str(item))
    words = nltk.word_tokenize(sentence)
