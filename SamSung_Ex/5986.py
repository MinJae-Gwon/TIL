T=int(input())
for i in range(T):
    N=int(input())
    l=[]
    for j in range(2,N+1):
        for k in range(1,j):
            if j%k:
                continue
            else:
                l.append(k)

print(l)
       


