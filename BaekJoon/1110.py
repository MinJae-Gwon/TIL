n = int(input())

def cycle(n):
    t=0
    new_n = 0
    while n!=new_n:
        cycle_1= n//10+n%10
        cycle_2= n%10*10+cycle_1%10
        new_n = cycle_2
        t+=1
    return t

print(cycle(n))

# if n<10:
#     n = int(str(n)+'0')
#     print(cycle(n))
# else:
#     print(cycle(n))


