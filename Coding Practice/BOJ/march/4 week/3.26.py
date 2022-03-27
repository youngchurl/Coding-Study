# 1. Boj 18870번 좌표 압축
# n = int(input())
# li = list(map(int, input().split()))
# tem = sorted(list(set(li)))
# dic = {i:j for j,i in enumerate(tem)}

# for i in li:
#     print(dic[i], end=' ')

'''
리뷰 : 딕셔너리로 바로 풀려서 뿌듯했다.
'''

# 2. Boj 1012번 유기농 배추
# import sys
# sys.setrecursionlimit(3000)
# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     mat = [[0]*m for _ in range(n)]

#     for _ in range(k):
#         a,b = map(int, input().split())
#         mat[b][a] = 1

#     def bug(x,y):
#         if x<0 or y>=m or y<0 or x>=n:
#             return 0
#         if mat[x][y] == 1:
#             mat[x][y] = 0
#             bug(x-1, y)
#             bug(x,y-1)
#             bug(x+1,y)
#             bug(x,y+1)
#             return 1
#         return 0
        
#     res = 0
#     for i in range(n):
#         for j in range(m):
#             res += bug(i,j)
#     print(res)

'''
리뷰 : 이문제가 안풀려서 BFS를 다시 공부해서 풀었다...
'''

# 3. Boj 2178번 미로탐색

n,m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]

def search(x,y,cnt):
    if x<0 or y<0 or x>=m or y>=n:
        return
    