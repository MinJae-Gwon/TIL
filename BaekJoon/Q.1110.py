origin_int = int(input())
res = 0
if origin_int < 10:
    two_digit_origin_int = origin_int*10
    i =0
    c =origin_int
    while origin_int == res:
            new_int = int(str(c)[0]) +int(str(c)[1])
            res = int(str(c)[-1]+str(new_int)[-1])
            origin_int = res
            i+=1
    print(i)
else:
    i =0
    c = origin_int
    while origin_int == res:
            new_int = int(str(c)[0]) +int(str(c)[1])
            res = int(str(c)[-1]+str(new_int)[-1])
            c = res
            i+=1
    print(i)

