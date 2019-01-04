T = int(input())

l=[]
for i in range(T):
    score = list(map(int,input().split()))
    l.append(score)

t=1
for i in l:
    i.sort()
    del i[0]
    del i[-1]
    print('#',t,' ',round(sum(i)/len(i)),sep='')
    t+=1
