# #sequence search
# l = list(map(int,input().split()))

# target = 2
# i=0
# while True:
#         if l[i] == target:
#                 print(f'검색완료 {i+1}번 째 :{l[i]}')
#                 break
#         else:
#                 i+=1

#         if i == len(l)-1 and l[i] != target:
#                 print(f'검색실패')
#                 break
                
# #binary search
# l = list(map(int,input().split()))
# target = 7
# start = 0
# end = len(l)-1
# while True:
#         mid = (start+end)//2
#         if l[mid] == target:
#                 print(f'search completed! at: {mid} index')
#                 break
#         elif l[mid] > target:
#                 end = mid -1
#         elif l[mid] < target:
#                 start = mid + 1
#         if start > end:
#                 print(f'search failed')

# selection sort
# l = list(map(int,input().split()))
# start = 0
# while True:
#         min_num = l[start]
#         for i in range(start, len(l)):
#                 if l[i] < min_num:
#                         min_num = l[i]
#                         min_num_idx = i
#         l[start], l[min_num_idx] = l[min_num_idx], l[start]
#         start+=1
#         if start == len(l)-1:
#                 break
# print(l)

# # cross
# l = [[0 for _ in range(5)] for _ in range(5)]
# for i in range(5):
#         l[i] = list(map(int,input().split()))

# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# def IsSafe(y,x):
#         if y>=0 and y<5 and x>=0 and x<5:
#                 return True
#         else:
#                 return False
# sum = 0
# for y in range(5):
#         for x in range(5):
#                 for dir in range(4):
#                         new_y = y + dy[dir]
#                         new_x = x + dx[dir]
#                         if IsSafe(new_y, new_x):
#                                 sum += abs(l[y][x] - l[new_y][new_x])
# print(sum)



