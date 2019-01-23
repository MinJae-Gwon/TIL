T=int(input())
for i in range(T):
    M=list(input())
    D=list('0'*len(M))
    res=0
    for j in range(len(M)):
        if M[j]==D[j]:
            pass
        else:
            for ele in range(j,len(M)):
                D[ele]=M[j]
            
            res+=1
    print(f'#{i+1} {res}')   


