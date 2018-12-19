#문제 2.
#자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

number = int(input('숫자를 입력하세요: '))
  
while True:    
    print(number%10)
    number = number//10
    if number %10 ==0:    
        break    


for i in range(number):
    print(i+1)

i=0
while i < number:
    print(i+1)
    i+=1