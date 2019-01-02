n = int(input())

ox_list = []
for i in range(n):
    a = input()
    ox_list.append(a)
count=0
sum=0
for i in ox_list:
    b = i.split('X')
    for j in b:
        count = j.count('O')
        for k in range(1,count+1):
            sum+=k
    
    print(sum)
    sum=0    


