test=[]
b=[]
l=[]

for i in range(int(input())):
    k=int(input())
    n=int(input())
    a=list(range(1,n+1))


    for i in range(k):
        for j in range(n):
            b.append(sum(a[:j+1]))
            
        l.append(b)
        a=b
        b=[]
    print(l[k-1][n-1])
    l=[]

