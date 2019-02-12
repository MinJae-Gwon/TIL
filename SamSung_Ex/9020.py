# import itertools

# T=int(input())
# for time in range(T):
#     a=int(input())
#     l=[x for x in range(1,a+1)]
#     l.insert(0,1)

#     for i in range(2,a+1):
#         j=2
#         while a>=i*j:
#             l[i*j]=1
#             j+=1
    
#     pure=[]
#     for ele in l:
#         if ele != 1:
#             pure.append(ele)
    

#     res_list= [ k for k in itertools.permutations(pure,2) if sum(k)==a ]
#     res_list.extend([(ele2,ele2) for ele2 in pure if 2*ele2==a])
    
#     res=()
#     for comb in res_list:
#         if not res:
#             res=comb
#         else:
#             if abs(res[0]-res[1]) > abs(comb[0]-comb[1]):
#                 res=comb
#     print(res[0],res[1])

number = [x for x in range(1,10001)]
number.insert(0,1)
for i in range(2,10001):
    j=2
    while 10000>=i*j:
        number[i*j]=1
        j+=1
n=int(input())
for i in range(n):
    a = int(input())
    div = a//2
    p = div
    q = div
    while p>0:
        if number[p] !=1 and number[q] !=1:
            if number[p]+number[q]==a:
                print(number[p],number[q])
                break
        p-=1
        q+=1
        
    



        

