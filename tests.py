from utils import  BagOfWords, load_pipeline

bag = BagOfWords('Желтый уровень опасности. Днем 4 сентября (пятница) местами по востоку республики ожидаются грозы.')
print(bag.months_bag)
print()
print()
print(bag.days_bag)

import pandas as pd

pipeline = load_pipeline('./pipelines/day_start_pipeline.pkl')
pred = pipeline.predict([bag.days_bag])
print(pred)