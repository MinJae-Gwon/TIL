for time in range(1,11):
    num = int(input())
    l = list(map(int,input().split()))
        
    while True:
        for i in range(1,6):
            l[0]=l[0]-i
                       
            if l[0]<=0:
                l[0]=0
                l.append(l[0])
                del l[0]
                break
            l.append(l[0])
            del l[0]
        if 0 in l:
            break
    l=list(map(str,l))
    res=' '.join(l)
    print(f'#{time} {res}')
        
    