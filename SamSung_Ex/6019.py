T=int(input())
for i in range(T):
    D,A,B,F=map(int,input().split())
    print(f'#{i+1} {D/(A+B)*20:0.10f}')