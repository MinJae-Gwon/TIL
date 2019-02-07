for time in range(1,11):
    N, ele = input().split()
    i=0
    N=int(N)
    ele=list(ele)

    while True:
        
        if ele[i]==ele[i+1]:
            del ele[i]
            del ele[i]
            if i<0:
                i=0
            else:
                i-=1
        else:
            i+=1
        if i==len(ele)-1:
            break  
          
    ele=''.join(ele)
    print(f'#{time} {ele}')     