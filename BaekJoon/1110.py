n = int(input())
origin_num = n
cycle2=-1
i=0
if n < 10:
    n = int('0'+str(n))
    origin_num=n
    while origin_num != cycle2:
        cycle1= n//10+n%10
        cycle2=int(str(n%10)+str(cycle1%10))
        n=cycle2
        i+=1
else:
    while origin_num != cycle2:
        
        cycle1= n//10+n%10
        cycle2=int(str(n%10)+str(cycle1%10))
        n=cycle2
        i+=1
print(i)