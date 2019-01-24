for time in range(10):
    T=int(input())
    l=[]
    for i in range(100):
        N=list(map(int,input().split()))
        l.append(N)
    
    #가로 합
    hor_max=0
    for ele_hor in l:
        sum_hor = sum(ele_hor)
        if sum_hor>hor_max:
            hor_max=sum_hor
    
    #세로 합
    ver_max=0

    for index_ver in range(100):
        ver_sum=0
        for ele_ver in l:
            ver_sum+=ele_ver[index_ver]
        if ver_sum>ver_max:
            ver_max=ver_sum
    
    #좌우 대각선 합
    diag_ele=0
    diag_sum=0
    while True:
        diag_sum+=l[diag_ele][diag_ele]
        diag_ele+=1
        if diag_ele>99:
            break
    
    #우좌 대각선 합
    re_diag_ele=0
    re_diag_index=99
    re_diag_sum=0
    while True:
        re_diag_sum+=l[re_diag_ele][re_diag_index]
        re_diag_ele+=1
        re_diag_index-=1
        if re_diag_ele>99:
            break
    
    max_num = max(hor_max,ver_max,diag_sum,re_diag_sum)
    
    print(f'#{time+1} {max_num}')

