import math

<<<<<<< HEAD
def numcheck(num):
    if num==1:
        return False
    n = int(math.sqrt(num))
    for i in (2,n+1):
        if num%i==0:
            return False
    return True
        
a,b=map(int,input().split())
print("a")
for j in range(a,b+1):
    if numcheck(j):
        print(j)

=======
def isPrime(num):
    if num==1:
        return False
    n = int(math.sqrt(num))
    for k in range(2,n+1):
        if num%k == 0:
            return False
    return True

m, n = map(int,input().split())
for k in range(m,n+1):
    if isPrime(k):
        print(k)
        
>>>>>>> bfe3f0a5df24f1354a0afdf64384298c7e28b66c
