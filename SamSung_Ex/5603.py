T=int(input())
for time in range(T):
    N=int(input())
    l=[]
    for S in range(N):
        s=int(input())
        l.append(s)
    origin_s = int(sum(l)/N)
    res=0
    for ele in l:
        res+=abs(ele-origin_s)
    res=int(res/2)
    print(f'#{time+1} {res}')
