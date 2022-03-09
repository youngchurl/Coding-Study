# 백준 1654번 랜선자르기

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# li = [int(input().rstrip()) for _ in range(n)]
# li2 = sorted(li)
# res = 0
# i = 1 

# while True:
#     tem = 0
#     if  li2[-1]//i < k:
#         for j in li:
#             tem += j//i
    
#     if tem == k-1:
#         res = i-1
#         break
#     i +=1
    
# print(res)


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [int(input().rstrip()) for _ in range(n)]
li.sort()
res = 0

l = 1
r = li[-1]
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for i in li:
        cnt += (i//mid)
    if cnt >=k:
        l = mid +1
    else:
        r = mid -1
    

print(r)