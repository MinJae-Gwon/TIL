T = int(input())

l=[]
for i in range(T):
    n = input()
    l.append(n)


t=1
for i in l:
    for j in range(2,16):
        if i[:j]== i[j:2*j]:
                        
            print(f'#{t}', len(i[:j]))
            t+=1
            break            
        else:
            continue
         

        
    

