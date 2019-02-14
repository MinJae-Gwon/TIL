for time in range(10):
    z = int(input())
    l=list(map(int,input().split()))
    res=0
    for i in range(2,z-1):
        if l[i] > l[i-1] and l[i] > l[i-2] and l[i] > l[i+1] and l[i] > l[i+2]:
            tall = max(l[i-2], l[i-2], l[i+1], l[i+2])
            res+=l[i] - tall
    print(res)        

