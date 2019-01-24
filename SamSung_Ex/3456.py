T=int(input())
for i in range(T):
    l=list(map(int,input().split()))
    for ele in l:
        if l.count(ele)==3:
            print(f'#{i+1} {ele}')
            break
        elif l.count(ele)==1:
            print(f'#{i+1} {ele}')