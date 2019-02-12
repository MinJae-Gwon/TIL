number = [x for x in range(1,1000001)]
number.insert(0,1)
for i in range(2,1000001):
    j=2
    while 1000000>=i*j:
        number[i*j]=1
        j+=1
    
res= [str(ele) for ele in number if ele != 1]
res=' '.join(res)
print(res)

