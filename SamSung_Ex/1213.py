for i in range(10):
    T=int(input())
    res=input()
    ex=input()
    count=0
    for j in range(len(ex)-len(res)+1):
        if res==ex[j:len(res)+j]:
            count+=1
    print(f'#{T} {count}')


        