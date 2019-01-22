T=int(input())
for i in range(T):
    res=0
    for j in range(int(input())):
        p,x=input().split()
        p=float(p)
        x=int(x)
        ave=p*x
        res+=ave
    print(f'#{i+1} {res:0.6f}')