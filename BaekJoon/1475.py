n = input()
six_count = n.count('6')
nine_count = n.count('9')
no_six_n = n.replace('6','')
no_n = no_six_n.replace('9','')

if six_count+nine_count==len(n):
    if (six_count+nine_count)%2==0:
        s= (six_count+nine_count)//2
        print(s)
    else:
        s= (six_count+nine_count)//2+1
        print(s)
else:
    if (six_count+nine_count)%2==0:
        s= (six_count+nine_count)//2
        count=[]
        for i in no_n:
            res=n.count(i)
            count.append(res)
        max_num=max(count)
        if max_num > s:
            print(max_num)
        else:
            print(s)
    else:
        s= (six_count+nine_count)//2+1
        count=[]
        for i in no_n:
            res=n.count(i)
            count.append(res)
        max_num=max(count)
        if max_num > s:
            print(max_num)
        else:
            print(s)


