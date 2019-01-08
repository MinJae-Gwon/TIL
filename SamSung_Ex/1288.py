T = int(input())
s = [0,1,2,3,4,5,6,7,8,9]
ship_list=[]
ship_int_list=[]
t=2


for i in range(T):
    n = int(input())
    
    origin_n = n


    while True:
        
        a = list(str(n))
       
        for j in a:
            ship_list.append(j)
            
        for k in ship_list:
            k = int(k)
            ship_int_list.append(k)
            

        ship_int_list = list(set(ship_int_list))
        
        if ship_int_list!=s:
            ship_list=[]
            n = t*origin_n    
            t+=1
            
        else:
            print(f'#{i+1} {n}')
            break
        


