## # Day04

## Dictionary

* dict.py

```python
# 1. 딕셔너리 만들기
lunch = { 
    '중국집': '02-345-4446',
    '양식집': '031-284-3573',
# 맨 뒤에 콤마 있어도 됨
}

dinner = dict(중국집='02-123-1234')
```

```python
# 2. 딕셔너리에 내용 추가하기
lunch['분식집'] = '053-123-1234'

# 3. 딕셔너리 내용 가져오기
print(lunch['중국집']) #=> '02-345-4446'
```

```python
#딕셔너리 안의 딕셔너리(중첩)
idol = {
    'bts':{
        '지민':24,
        'RM':25
    }
}
idol['bts']#=> {'지민':24,'RM':25}
idol['bts']['RM']#=> 25
```

```python
# 4. 딕셔너리 반복문 활용하기
#(1)기본활용
for key in lunch:
    print(key)#=> key
    print(lunch[key])#=> value

#(2)키만 가져오기
for key in lunch.keys():
    print(key)#=>list와 유사한 형태 출력

 #(3)value만 가져오기
for value in lunch.values():
     print(value)   

#(4)item item(key, value) 가져오기: .items()
# lunch.items() #=> [('중식', '02'),...]
for key, value in lunch.items():
    print(key, value)
```

```python
#2개 = 자료형(list, tuple ...) 길이2
a,b = (1,2)
print(a) #=>1
print(b) #=>2
```

```python
#연습문제
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 1. 이 학생의 평균을 구하시오.
#풀이 1
total_score =0
for subject_score in score.values():
    total_score = total_score + subject_score

ave_score = total_score / len(score)
print(ave_score)

#풀이 2
total_score = sum(score.values())
ave_score = total_score / len(score)
print(ave_score)

# 2. 반평균을 구하시오
# 1. 나의 풀이
total_score = 0
list_score = []
for value1 in score.values():
    for value2 in value1.values():
        total_score = total_score + value2
for value1 in score.values():
    for key in value1.keys():
        print(key)
        for i in key:
            list_score.append(i)

print(list_score)        
print(len(key))
ave_score = total_score / len(list_score)
print(ave_score)        
        
# 2. 쌤 풀이

total_score = 0
count = 0
for person_score in score.values():
    for subject_score in  person_score.values():
        total_score += subject_score
        count +=1
ave_score = total_score / count
print(ave_score)

# 3. 도시별 최근 3일의 온도입니다.
city ={
    '서울':[-6, -10, 6],
    '대전':[-3, -10, 2],
    '광주':[0, -2, 10],
    '구미':[2, -2, 9]
}
# 3-1. 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
구미 : 값
'''

int_temp =[]
for city_temp in city.values():
    total=0
    print(city_temp)
    for total_city_temp in city_temp:
        total = total + total_city_temp
        print(total)

```

```
city ={
    '서울':[-6, -10, 6],
    '대전':[-3, -10, 2],
    '광주':[0, -2, 10],
    '구미':[2, -2, 9]
}
# 3-1. 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
구미 : 값
'''
# 내 답
i=0
int_temp =[]
citylist = list(city.keys())
for city_temp in city.values():
    total=0
    for total_city_temp in city_temp:
        total = total + total_city_temp
    print(citylist[i] , total/len(city.values()))
    i+=1

# 쌤 답
for name, temp in city.items():
    #name #=>'서울'
    #temp #=>[-6,-10,6]
    total_temp = 0
    for t in temp:
        total_temp+=t
ave_temp = total_temp / len(temp) #=> -10/3

# 3-2. 가장 더웠던 곳은?

city_max = 0
top_temp = []
for city_temp in city.values():
    print(city_temp)
    city_max = max(city_temp)
    top_temp.append(city_max)
print(max(top_temp))
```

* dict_adv.py

```python
import random
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}

#난이도 * 
# 1. 지역(location)은 몇개 있나요? : list length
# 출력예시) 4
print(len(ssafy['location']))

#난이도** 
# 2. python standard library에 'requests'가 있나요? : 접근 및 list in
#출력예시) false
if 'request' in ssafy['language']["python"]['python standard library']:
    print('true')
else:
    print('False')

#난이도** 
# 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근
#출력예시)엄윤주
print(ssafy['classes']['gm']['class president'])

#난이도*** 
# 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
#출력 예시)python web
for langs in ssafy['language'].keys():
    print(langs)

#난이도*** 
# 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
#출력 예시)change pro-gj  
for name in ssafy['classes']['gj'].values():
    print(name)

#난이도***** 
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
#출력 예시)flask는 micro이다. django는 full-functioning이다.    
for a,b in ssafy['language']['python']['frameworks'].items():
    print(f'{a}는{b}이다')

#난이도***** 
# 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
#출력예시)오늘의 당번은 하창언
group_list =ssafy['classes']['gm']['groups']['4조']
print(random.choice(group_list))

#번외
#모든 그룹 중에 한명을 랜덤으로 뽑아 주세요
#민재는 박머갈 = TRUE
#광광 우럭탁! = TRUE
empty = []
for i in ssafy['classes']['gm']['groups'].values():
    empty.append(i)
print(random.choice(random.choice(empty)))

#Chain
print(random.choice(random.choice(list(ssafy['classes']['gm']['groups'].values()))))
```





