t=int(input())

l=[]
for i in range(t):
    n = int(input())
    l.append(n)

t=1
sum =0
for i in l:
    for j in range(1,i+1):
        if j%2==1:
            sum+=j
        else:
            sum-=j
    print(f'#{t} {sum}')
    t+=1
    sum=0