n = int(input())

if n < 5:
    if n==3:
        print(1)
    else:
        print(-1)
elif n>=5:
    if n%5==0:
        print(n//5)
    elif n%5!=0:
        if (n%5)%3==0:
            print(n//5+n%5//3)
        elif (n%5)%3 !=0:
            if n%3 ==0:
                print(n//3)
            elif (n%3)%5 ==0:
                print(n//3+n%3//5)
            
                print(-1)
        else:
            print(-1)   
                   