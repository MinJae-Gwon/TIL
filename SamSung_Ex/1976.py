T=int(input())
for i in range(T):
    h1,m1,h2,m2=map(int,input().split())
    H=h1+h2
    M=m1+m2
    if M>59:
        M=M-60
        H+=1
        if H>11:
            H=H-12
    else:
        if H>11:
            H=H-12

    print(f'#{i+1} {H} {M}')


    