from utils import  BagOfWords, load_pipeline
import csv

# bag = BagOfWords('Оранжевый уровень опасности. В дневные часы 8 и 9 июня (понедельник-вторник) по юго-востоку во многих районах, а на остальной')
# print(bag.months_bag)
# print()
# print()
# print(bag.days_bag)

import pandas as pd

# pipeline = load_pipeline('./pipelines/day_start_pipeline.pkl')
# pred = pipeline.predict([bag.days_bag])
# print(pred)

pipeline_month = load_pipeline('./pipelines/month_pipeline.pkl')
pipeline_day_start = load_pipeline('./pipelines/day_start_pipeline.pkl')
pipeline_day_end = load_pipeline('./pipelines/day_end_pipeline.pkl')

with open('test_data.csv', encoding='utf-8',  newline='') as csvfile:
  reader = csv.DictReader(csvfile, delimiter=';')
  for row in reader:
      bag = BagOfWords(row['text'])
      print(row['text'])
      print('------')
      print('month')
      print(pipeline_month.predict([bag.months_bag]))
      print('day_start')
      print(pipeline_day_start.predict([bag.days_bag]))
      print('day_end')
      print(pipeline_day_end.predict([bag.days_bag]))
