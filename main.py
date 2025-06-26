import csv

with open('res/map.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        print(f"Старт: {row[0]}, Конец: {row[1]}")