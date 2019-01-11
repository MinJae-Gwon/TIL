n =int(input('입력: '))
s=[]
while True:
    if n//2==1:
        s.append(n%2)
        s.append(1)
        break
    elif n==1:
        s.append(1)
        break    
    else:
        s.append(n%2)
        n = n//2

s.reverse()    
for i in s:
    print(i,end='')