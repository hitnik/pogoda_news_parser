from utils import  BagOfWords

bag = BagOfWords('Желтый уровень опасности. Днем 4 сентября (пятница) местами по востоку республики ожидаются грозы.')
print(bag.get_months_bag())
print()
print()
print(bag.get_days_bag())