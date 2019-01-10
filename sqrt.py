def right(n):
    i=1
    while True:
        if i**2 >n:
            return i
        else:
            i+=1

def left(n):
    i=1
    while True:
        if i**2<=n:
            i+=1
            if i**2>=n:
                return i-1
                     
        else:
            return i-1
            
def sqrt(n,l,r):
    while round(l,3)!=round(r,3):
        if ((l+r)/2)**2 > n:
            r = (l+r)/2
        elif ((l+r)/2)**2 < n:
            l = (l+r)/2
        elif ((l+r)/2)**2==n:
            return ((l+r)/2)           
    return round(l,3)

n=int(input('수를 입력하세요: '))
l=left(n)
r=right(n)
print(sqrt(n,l,r))
