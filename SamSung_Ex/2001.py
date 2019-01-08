T = int(input())
for t in range(T):

    N,M = map(int,input().split())
    l=[]
    for i in range(N):
        n = list(map(int,input().split()))
        l.append(n)

    max_num=0
    result=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                result+=sum(l[i+k][j:j+2])
            
            if result>max_num:
                max_num=result
                result=0
            else:
                result=0
    print(f'#{t+1} {max_num}')