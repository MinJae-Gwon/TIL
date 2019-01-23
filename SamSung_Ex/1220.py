for time in range(1):
    T=int(input())
    l=[]
    for i in range(T):
        line=list(input().split())
        l.append(line)

#2차원 배열 오른쪽 90도 회전    
    new_l = []
    new_line = ''
    for index in range(T):
        for jul in l:
            new_line += jul[index]
        new_line=list(new_line)
        new_l.append(new_line)
        new_line=''
    print(new_l)

#1,2 하나 있는 줄 없애기   
    idx=0
    while idx!=len(new_l):
        ele1 = new_l[idx]
        if ele1.count('0')==T-1:
            new_l.remove(ele1)
            idx-=1
        idx+=1
    print(new_l)

#2(blue)없애기
    for ele2 in new_l:
        for index_two,two in enumerate(ele2):
            
            if two=='1':
                break
            elif two=='2':
                ele2[index_two]='0'
        
    print(new_l)

#1(red)없애기
    for ele3 in new_l:
        for index_one in range(-1,-len(ele3),-1):
            if ele3[index_one]=='2':
                break
            elif ele3[index_one]=='1':
                ele3[index_one]='0'
    print(new_l)
    
#충돌
    for ele4 in new_l:
        ele4=''.join(ele4)
    print(new_l)