n = int(input())

def cycle(n):
    t=0
    new_n = n
    while n!=new_n:
        cycle_1= new_n//10+new_n%10
        cycle_2= int(str(new_n%10)+str(cycle_1%10))
        new_n = cycle_2
        t+=1
    return t

print(cycle(26))
# if n<10:
#     n = int(str(n)+'0')
#     print(cycle(n))
# else:
#     print(cycle(n))


