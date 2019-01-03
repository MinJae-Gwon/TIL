T=int(input())
l=[]
for i in range(T):
    n = input()
    l.append(n)
t=1
for i in l:
    word = list(i)
    r = list(reversed(word))
    
    if word==r:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
    t+=1    