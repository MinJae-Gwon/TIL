T=int(input())
for i in range(T):
    N=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l=[str(x) for x in l]
    res=' '.join(l)
    print(f"#{i+1} {res}")