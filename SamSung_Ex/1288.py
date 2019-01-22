import copy
T=int(input())
for j in range(T):
    N=int(input())
    origin_N=copy.deepcopy(N)
    num_list=[]
    i=1
    while True:
        N=i*origin_N
        split_N=list(str(N))
        num_list.extend(split_N)
        num_list=list(set(num_list))
        i+=1
        if len(num_list)==10:
            break
    print(f'#{j+1} {N}')


























# s = [0,1,2,3,4,5,6,7,8,9]
# ship_list=[]
# ship_int_list=[]
# t=2


# for i in range(T):
#     n = int(input())
    
#     origin_n = n

#     while True:
        
#         a = list(str(n))
       
#         for j in a:
#             ship_list.append(j)
            
#         for k in ship_list:
#             k = int(k)
#             ship_int_list.append(k)
          
#         ship_int_list = list(set(ship_int_list))
        
#         if ship_int_list!=s:
#             ship_list=[]
#             n = t*origin_n    
#             t+=1
            
#         else:
            
#             break
        


