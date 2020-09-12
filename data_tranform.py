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

#
# bag = set()
# for i in range(1,32):
#     bag.add(str(i))
#     if i < 31:
#         bag.add(str(i)+'-'+str(i+1))
#
# with open('weather_data_3.csv', encoding='utf-8', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     row_names = next(reader)
#     row_names.remove('day_start')
#     row_names.remove('day_end')
#     row_names.remove('text')
#     row_names.remove('month')
#
# with open('weather_data_3.csv', encoding='utf-8', newline='') as csvfile:
#     bag_dict = {}
#     dict_list = []
#     reader_2 = csv.DictReader(csvfile)
#     for row in reader_2:
#         print(row)
#         row_dict = {}
#         for item in bag:
#             bag_dict[item] = 0
#         for name in row_names:
#             for k,v in bag_dict.items():
#                 for mon in MONTHS_GEN.values():
#                     pattern = k+mon
#                     if pattern == name:
#                         bag_dict[k] += int(row[name])
#         if 0 < int(row['day_start']) <= 31:
#             row_dict['text'] = row['text']
#             row_dict.update(bag_dict)
#             row_dict['day_start'] = row['day_start']
#             row_dict['day_end'] = row['day_end']
#             dict_list.append(row_dict)
#     with open('weather_data_days.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(k for k, v in dict_list[0].items())
#         for d in dict_list:
#             print(d)
#             writer.writerow(v for k, v in d.items())

import pprint

pp = pprint.PrettyPrinter(width=100)

with open('weather_data_days.csv', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    row_names = next(reader)
    row_names.remove('day_start')
    row_names.remove('day_end')
    row_names.remove('text')

    print(row_names)

dict_list = []

with open('weather_data_days.csv', encoding='utf-8', newline='') as csvfile:
    reader_2 = csv.DictReader(csvfile)
    cont = True
    for row in reader_2:
        day_start = row['day_start']
        day_end = row['day_end']
        row_dict = {}
        row_dict['text'] = row['text']
        check_list = []
        if cont:
            for name in row_names:
                row_dict[name] = row[name]
                if int(row[name]) > 0:
                    try:
                        check_list.append(int(name))
                    except ValueError:
                        if re.match(r'^\d+-\d+', name):
                            check_list.append(int(re.split('-', name)[0]))
            if len(check_list) > 0 and not int(row['day_start']) in check_list:
                print('--------')
                print('day-start  :  '+  row['day_start'])
                print('--------')
                print('check_list')
                print(check_list)
                print('--------')
                pp.pprint(row['text'])
                print('day_start : ')
                day_start = input()
                print('day_end : ')
                day_end = input()
                print('--------')
                print('Exit? (0 - exit, Eny other key to continue)')
                try:
                    cont = (bool(int(input())))
                except ValueError:
                    cont = True
        else:
            for name in row_names:
                row_dict[name] = row[name]
        row_dict['day_start'] = day_start
        row_dict['day_end'] = day_end
        dict_list.append(row_dict)
with open('weather_data_days.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(k for k, v in dict_list[0].items())
    for d in dict_list:
        print(d)
        writer.writerow(v for k, v in d.items())

