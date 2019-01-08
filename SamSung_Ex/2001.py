l = [[1, 3, 3, 6, 7],
[8, 13, 9, 12, 8],
[4, 16, 11, 12, 6],
[2, 4, 1, 23, 2],
[9, 13, 4, 7, 3]]

N=5
M=2
max_num=0
result=0
for i in range(N-M+1):
    for j in range(N-M+1):
        for k in range(M):
            result+=sum(l[i+k][j:j+2])
        
        if result>max_num:
            max_num=result
            result=0
        else:
            result=0
print(max_num)