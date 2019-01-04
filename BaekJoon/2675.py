T = int(input())
l=[]
for i in range(T):
    n=input().split()
    l.append(n)

for i in l:
    num=i[0]
    alpha=i[1]
    for j in alpha:
        print(j*int(num),end='')  
    print('')