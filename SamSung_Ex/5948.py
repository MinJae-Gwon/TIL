from itertools import combinations
T=int(input())
for i in range(T):
    
    test_list=list(map(int,input().split()))
    comb_list=list(combinations(test_list,3))
    
    sum_num_list =[sum(x) for x in comb_list]
    sum_num_list=list(set(sum_num_list))
    sum_num_list.sort()
    
    ans = sum_num_list[-5]
    print(f'#{i+1} {ans}')
