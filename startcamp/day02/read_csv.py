import csv

with open('lunch.csv','r', encoding='utf8') as f:
    items = csv.reader(f) #한 줄씩리스트 형대로 반환
    for item in items:
        print(item)