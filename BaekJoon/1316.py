res=0
for i in range(int(input())):
    n=input()
    n=list(n)
    for i in n:
        if n.count(i)==1:
            continue
        else:
            for j in range(n.count(i)-1):
                front=n.index(i)
                if n.index(i,front+1)-n.index(i,front)>1:
                    res-=1
                    break
                else:
                    n.remove(i)
            res+=1
        res+=1
print(res)

        