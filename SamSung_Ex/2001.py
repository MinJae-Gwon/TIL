T = int(input())
N,M = map(int,input().split())
l=[]
for i in range(N):
    t = list(map(int,input().split()))
    l.append(t)

max_num=0
result=0
for number in range(N+1):
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                result+=sum(l[k][j:j+2])
            if result>max_num:
                max_num=result
print(max_num)


