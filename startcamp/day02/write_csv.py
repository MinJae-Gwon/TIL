lunch = {
    '둥지': '031-244-4567',
    '신가네': '032-395-9356',
    '이모네': '02-314-2245'
}

import csv

with open('lunch.csv', 'w', encoding='utf8',newline='') as f: #newline = 빈 줄 없이 출력
    csv_writer = csv.writer(f) #f는 파일 내용
    for item in lunch.items(): #리스트 [(key,value),...]
        csv_writer.writerow(item)
        #f.write(f'{item[0]}, {item[1]}\n') => csv_writer = csv.writer(f) 안쓸때