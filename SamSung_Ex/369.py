n = int(input())

sum = 0
a=0
b=0
c=0
for i in range(1,n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        
        a = str(i).count('3')
        b = str(i).count('6')
        c = str(i).count('9')
        sum = a+b+c
        i = '-'*sum
    print(i,end=' ')

