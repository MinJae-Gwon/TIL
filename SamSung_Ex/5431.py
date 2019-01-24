T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    good_l = list(map(int,input().split()))
    all_l=[x for x in range(1,N+1)]
    for j in good_l:
        if j in all_l:
            all_l.remove(j)
        else:
            pass
    all_l=[str(k) for k in all_l]
    res=' '.join(all_l)
    print(f'#{i+1} {res}') 
    