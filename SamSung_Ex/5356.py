T=int(input())
for time in range(T):
    l=[]
    for k in range(5):
        a=input()
        l.append(a)
    max_len=0
    for ele in l:
        if len(ele)>max_len:
            max_len=len(ele)
    
    for ele2 in range(len(l)):
        if len(l[ele2]) < max_len:
            l[ele2]+=' '*(max_len-len(l[ele2]))
    
    res=''
    for i in range(max_len):
        for j in range(5):
           
            if l[j][i]:
                res+= l[j][i]
    res=res.replace(' ','')            
    print(f'#{time+1} {res}')
