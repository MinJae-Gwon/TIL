def palin(n):
    
    if len(n)==1:
        return True
    elif len(n)%2==0:
        for i in range(len(n)//2):
            if n[i] != n[len(n)-1-i]:
                return False
        return True
    else:
        for j in range(len(n)//2):
            if n[j] != n[len(n)-1-j]:
                return False
        return True
                
print(palin('naana'))