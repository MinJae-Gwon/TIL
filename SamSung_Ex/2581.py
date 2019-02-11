M=int(input())
N=int(input())
l=list(range(M,N+1))
res=[]
for i in l:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        res.append(i)
if not res:
    print(-1)
else:
    print(sum(res))
    print(min(res))

