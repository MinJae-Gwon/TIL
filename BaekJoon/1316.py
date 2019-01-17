import copy
res=0
for i in range(int(input())):
    n=input()
    deep_n=copy.deepcopy(list(n))
    n=list(n)
    if len(set(n))==len(n):
        res=1
    else:
        for i in deep_n:
            if n.count(i)==1:
                n.remove(i)
            else:
                for j in range(n.count(i)-1):
                    front=n.index(i)
                    if n.count(i)==1:
                        n.remove(i)
                    elif n.index(i,front+1)-n.index(i,front)>1:
                        res-=1
                        break
                    elif n.index(i,front+1)-n.index(i,front)==1:
                        n.remove(i)
        res+=1                
print(res)

        