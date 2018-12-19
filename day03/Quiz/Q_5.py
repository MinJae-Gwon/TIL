# 문제 5.
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# # 입력 예시: 300000;20000;10000
# '''

prices = input('물품 가격을 입력하세요: ')
a=prices
b=a.split(';')

b = list(map(int, b))
# #1. b = [int(i) for i in b]
# #2. for i in range(len(b)):
# #       b[i] = int(b[i])
b.sort()
#b=sorted(b,key=int)
b.reverse()
# #b.sort(reverse=True) 가능
print(b)




# while문 이용으로 풀기
#find함수로 ; 찾은 후 반복 슬라이싱
# if  a != 0:
#     b=a
#     print(prices[a+1:])




