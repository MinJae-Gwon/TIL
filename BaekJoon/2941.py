n = input()

cro_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count=0
for i in cro_list:
    count+=n.count(i)
    n = n.replace(i,' ')
print(n)
print(count+len(list(n))-list(n).count(' '))
