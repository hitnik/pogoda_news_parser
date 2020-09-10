import csv
import re
from utils import sentence_to_bagofwords
from utils import MONTHS_GEN

# with open('weather_forecast_2.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         text = row['text']
#         sentence_to_bagofwords(text)

# bag = set()
#
# for i in range(1,32):
#     for month in MONTHS_GEN.values():
#         bag.add(str(i)+month)
#         if i < 31:
#             bag.add(str(i)+'-'+str(i+1)+month)
#
# with open('words_bag_2.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["bag"])
#     for word in bag:
#         writer.writerow([word])
# print(bag)


# d_list = []
# with open('weather_forecast.csv', encoding='utf-8', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         text = row['text']
#         print(text)
#         month = row['month']
#         days = row['days']
#         days = days.replace('[', '')
#         days = days.replace(']', '')
#         days = days.replace(' ', '')
#         day_list = days.split(',')
#         d = {}
#         d['text'] = text
#         d.update(sentence_to_bagofwords(text))
#         d['month'] = month
#         d['day_start'] = day_list[0]
#         if len(day_list) > 1:
#             d['day_end'] = day_list[1]
#         else:
#             d['day_end'] = day_list[0]
#         d_list.append(d)
# with open('weather_data_3.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(k for k, v in d_list[0].items())
#     for d in d_list:
#         print(d)
#         writer.writerow(v for k, v in d.items())



# with open('weather_data_3.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     row_names = next(reader)
#     row_names.remove('day_start')
#     row_names.remove('day_end')
#     row_names.remove('text')
#     row_names.remove('month')
# with open('weather_data_3.csv', newline='') as csvfile:
#     month_dict = {}
#     dict_list = []
#     reader_2 = csv.DictReader(csvfile)
#     for row in reader_2:
#         row_dict = {}
#         for month in MONTHS_GEN.values():
#             month_dict[month] = 0
#         for name in row_names:
#             for k,v in month_dict.items():
#                 pattern = re.compile(k+'$')
#                 if re.search(pattern, name):
#                     month_dict[k] += int(row[name])
#         row_dict['text'] = row['text']
#         row_dict.update(month_dict)
#         row_dict['month'] = row['month']
#         dict_list.append(row_dict)
#     with open('weather_data_month.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(k for k, v in dict_list[0].items())
#         for d in dict_list:
#             print(d)
#             writer.writerow(v for k, v in d.items())


bag = set()
for i in range(1,32):
    bag.add(str(i))
    if i < 31:
        bag.add(str(i)+'-'+str(i+1))
