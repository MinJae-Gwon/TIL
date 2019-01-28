for time in range(10):
    g=int(input())
    l=[]
    for ROW in range(8):
        row=input()
        l.append(row)
    res=0
    # 가로
    for row_comp in l:
        for i in range(8-g+1):
            palin=row_comp[i:i+g]
            re_palin=list(reversed(palin))
            print(palin)
            print('_______________________')
            print(re_palin)
            if palin == re_palin:
                res+=1
    print(res)
    # # 세로
    # for j in range(8-g+1):
        

