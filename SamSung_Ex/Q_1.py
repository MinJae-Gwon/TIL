#10개의 수를 입력 받아 홀수만 더하라

a = map(int, input().split())
b=list(a)
c=0
for i in b:
    if i%2==1:
        c+=i
print(c) 





    
