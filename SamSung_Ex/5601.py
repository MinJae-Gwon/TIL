T=int(input())
for i in range(T):
    N=input()
    l=[]
    for j in range(int(N)):
        res='1/'+N
        l.append(res)
    l=' '.join(l)
    print(f'#{i+1} {l}')
