from utils import  BagOfWords

bag = BagOfWords('Желтый уровень опасности. Днем 4 сентября (пятница) местами по востоку республики ожидаются грозы.')
print(bag.months_bag)
print()
print()
print(bag.days_bag)

import pandas as pd
