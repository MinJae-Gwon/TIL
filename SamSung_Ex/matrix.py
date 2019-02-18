# l=[[1,2,3],[4,5,6],[7,8,9]]

# a=list(zip(*l))

# print(a)

l=[10,12,2,7,5,3]

for i in range(len(l)-1):
    min=i
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            min=j
    l[i],l[min]=l[min],l[i]
print(l)