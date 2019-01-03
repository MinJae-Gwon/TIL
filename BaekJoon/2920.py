n = list(map(int,input().split()))
r = list(reversed(list(range(1,len(n)+1))))

if n == list(range(1,len(n)+1)):
    print('ascending')
elif n== r:
    print('descending')
else:
    print('mixed')