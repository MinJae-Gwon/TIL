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

maxi =0
int_temp =[]
for city_temp in city.values():
    print(city_temp)
    for i in city_temp:
        city_max = max(city_temp)
        
    print(city_max)
       
       
# 3-3. 