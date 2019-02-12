T=int(input())
for time in range(T):
    a=list(input())
    H=int(input())
    l=sorted(list(map(int,input().split())))
    i=0
    for idx in l:
        a.insert(idx+i,'-')
        i+=1
    a=''.join(a)
    print(f'#{time+1} {a}')

