T=int(input())
for i in range(T):
    N=input()
    v='aeiou'
    for vowel in v:
        if vowel in N:
            N=N.replace(vowel,'')
    print(f'#{i+1} {N}')
            

            