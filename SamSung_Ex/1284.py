T=int(input())
for i in range(T):
    P,Q,R,S,W=map(int,input().split())
    A=P*W
    if W<=R:
        B=Q
        print(f'#{i+1} {min(A,B)}')
    else:
        B=Q+(W-R)*S
        print(f'#{i+1} {min(A,B)}')
        