T=int(input())
for time in range(T):
    a=int(input())
    if a%2==0:
        print(f'#{time+1} Even')
    else:
        print(f'#{time+1} Odd')