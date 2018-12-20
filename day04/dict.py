# 1. 딕셔너리 만들기
lunch = { 
    '중국집': '02-345-4446',
    '양식집': '031-284-3573',
# 맨 뒤에 콤마 있어도 됨
}

dinner = dict(중국집='02-123-1234')

# 2. 딕셔너리에 내용 추가하기
lunch['분식집'] = '053-123-1234'

# 3. 딕셔너리 내용 가져오기
print(lunch['중국집']) #=> '02-345-4446'

#딕셔너리 안의 딕셔너리(중첩)
idol = {
    'bts':{
        '지민':24,
        'RM':25
    }
}
idol['bts']#=> {'지민':24,'RM':25}
idol['bts']['RM']#=> 25

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

#2개 = 자료형(list, tuple ...) 길이2
a,b = (1,2)
print(a) #=>1
print(b) #=>2

#연습문제
score = {
    'a' : {
    '수학': 80,
    '국어': 90,
    '음악': 100
    },
    'b' : {
    '수학': 80,
    '국어': 90,
    '음악': 100
    }
}

# # 1. 이 학생의 평균을 구하시오.
# #풀이 1
# total_score =0
# for subject_score in score.values():
#     total_score = total_score + subject_score

# ave_score = total_score / len(score)
# print(ave_score)

# #풀이 2
# total_score = sum(score.values())
# ave_score = total_score / len(score)
# print(ave_score)


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
total =0
int_temp =[]
for city_temp in city.values():
    total=0
    print(city_temp)
    for total_city_temp in city_temp:
        total = total + total_city_temp
        print(total)
        