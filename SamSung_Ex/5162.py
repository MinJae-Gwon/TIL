T=int(input())
for time in range(T):
    A,B,C=map(int,input().split())
    res=0
    if A>B:
        res+=C//B
        if C%B !=0 and C%B//A>=1:
            res+=C%B//A
    elif A<B:
        res+=C//A
        if C%A !=0 and C%A//B >=1:
            res+=C%A//B
    else:
        res+=C//A
    print(f'#{time+1} {res}')
