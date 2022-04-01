# 1. 18111번 마인크래프트
# import sys
# input = sys.stdin.readline
# n, m, k = map(int, input().split())
# mat = [list(map(int, input().split())) for _ in range(n)]
# h = 0
# ans = 1000000000000000000000000
# for i in range(257):
#     mini = 0
#     maxi = 0
#     for y in range(n):
#         for x in range(m):
#             if mat[y][x] > i:
#                 mini += mat[y][x] - i
#             else:
#                 maxi += i-mat[y][x]
    
#     inven = k+mini
#     if inven < maxi:
#         continue

#     time = mini*2 + maxi
#     if time <= ans:
#         ans = time
#         h = i

# print(ans, h)

'''
리뷰: 문제가 안풀려서 대략 일주일동안 답보면서 공부했다...
구현 방법 자체는 알겠는데 continue가 익숙하지 않아서 어려웠던 문제다
'''

# 2. 1074번 Z
# n,r,c = map(int, input().split())
# mat = [[0]*(n**2) for _ in range(n**2)]
# cnt = 0
# def zspace(li):
#     global cnt
#     if len(li) ==2:
#         for i in range(2):
#             for j in range(2):
#                 li[i][j] +=cnt
#                 cnt +=1
#     else:
#         num = len(li)
#         tem = [li[i][:num//2] for i in range(0,num//2)]
#         zspace(tem)
#         tem = [li[i][:num//2] for i in range(num//2,num)]
#         zspace(tem)
#         tem = [li[i][num//2:num] for i in range(0,num//2)]
#         zspace(tem)
#         tem = [li[i][num//2:num] for i in range(num//2,num)]        
#         zspace(tem)

# print(zspace(mat))
# print(mat[r][c])

# 3. 1697번 숨바꼭질
n, k = map(int, input().split())
res = n
cnt = 0
while res !=k:
