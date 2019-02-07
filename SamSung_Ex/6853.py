T = int(input())
for time in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    N=int(input())
    outside_res=0
    online_res=0
    inside_res=0
    for i in range(N):
        x,y = map(int,input().split())
        if x<x1 or y<y1 or x>x2 or y>y2:
            outside_res+=1
        elif (x1-x2>=x and y==y1) or (x1-x2>=x and y==y2) or (y2-y1>=y and x==x1) or (y2-y1>=y and x==x2):
            online_res+=1
        else:
            inside_res+=1
    print(f'#{time+1} {inside_res} {online_res} {outside_res}')