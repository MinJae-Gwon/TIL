l=[]
for i in range(5):
    n = int(input())
    l.append(n)


for i in range(5):
    if l[i] < 40:
        l[i] = 40

ave = sum(l)/5
print(int(ave))
        
    
