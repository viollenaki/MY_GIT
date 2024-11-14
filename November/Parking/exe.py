# 1. Рассчитайте общее количество каждого автомобиля на парковке.
# Используя данные из файлов parking_data.csv и cars.csv,
#  напишите программу, которая рассчитывает общее количество каждого автомобиля,
#  припаркованного на различных парковках. Выведите список автомобилей с количеством парковок для каждого.
from collections import defaultdict
from csv import reader
with open(r'C:\Users\User\Desktop\GIT AIT Akbar\November\Parking\cars.csv', encoding='utf-8') as cars:
    car_type = {}
    cars = list(reader(cars))[1:]
    for num, type in cars:
        car_type[num] = type

with open(r'C:\Users\User\Desktop\GIT AIT Akbar\November\Parking\parking_data.csv', encoding='utf-8') as parking_data:
    parking_data = list(reader(parking_data))[1:]


# print(car_type['EE7174FF'])

def get_every_car_count():
    dict = {}
    for _,car,_,_,sid in parking_data:
        dict[sid] = dict.get(sid, {})
        dict[sid][car_type[car]] = dict[sid].get(car_type[car], 0) + 1
    return dict
print(get_every_car_count())
     

