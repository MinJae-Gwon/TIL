#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

input = list(map(int,input().split())
count =0
total =0
for number in input:
    total+=number
    count+=1

ave = total_num / len(input)
print(ave)

