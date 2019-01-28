T=int(input())
for time in range(T):
    N,K = map(int,input().split())
    l=list(map(int,input().split()))
    l=sorted(l,reverse=True)
    res=sum(l[:K])
    print(f'#{time+1} {res}')
