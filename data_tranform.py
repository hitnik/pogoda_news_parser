import csv
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



d_list = []
with open('weather_forecast_2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text = row['text']
        date_start = row['date_start']
        date_end = row['date_end']
        d = {}
        d['text'] = text
        d.update(sentence_to_bagofwords(text))
        d['date_start'] = date_start
        d['date_end'] = date_end
        d_list.append(d)
with open('weather_data_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(k for k, v in d_list[0].items())
    for d in d_list:
        writer.writerow(v for k, v in d.items())