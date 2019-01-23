T=int(input())
for i in range(T):
    N,M = map(int,input().split())
     
    for x in range(0,M+1):
        for y in range(0,M+1):
            if x+y==M and 2*x+y==N:
                break
        if x+y==M and 2*x+y==N:
                break
    print(f'#{i+1} {y} {x}')        