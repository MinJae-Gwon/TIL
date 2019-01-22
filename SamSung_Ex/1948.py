dic={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

T=int(input())
for i in range(T):
    fm,fd,bm,bd=map(int,input().split())
    if bm-fm==0:
        print(f'#{i+1} {bd-fd+1}')
    else:
        res=0
        for key in range(fm,bm):
            res+=dic[key]
        print(f'#{i+1} {res+bd-fd+1}')
