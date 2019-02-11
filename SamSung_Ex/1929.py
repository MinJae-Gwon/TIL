import math

def numcheck(num):
    if num==1:
        return False
    n = int(math.sqrt(num))
    for i in (2,n+1):
        if num%i==0:
            return False
    return True
        
a,b=map(int,input().split())

for j in range(a,b+1):
    if numcheck(j):
        print(j)

