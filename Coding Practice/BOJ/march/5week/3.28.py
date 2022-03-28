# 1. 2630번 색종이 만들기
# n = int(input())
# mat = [list(map(int, input().split())) for _ in range(n)]
# res = []

# def cut(x,y,n):
#     color = mat[x][y]

#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != mat[i][j]:
#                 cut(x,y,n//2)
#                 cut(x,y+n//2,n//2)
#                 cut(x+n//2,y,n//2)
#                 cut(x+n//2,y+n//2,n//2)
#                 return
#     if color == 1:
#         res.append(1)
#     else:
#         res.append(0)
# cut(0,0,n)
# print(res.count(0))
# print(res.count(1))

'''
리뷰: 분할 정복이라는 생소한 개념이 등장했다. 의미는 알겠는데 그걸 구현하려고
생각하니 막막함이 들어서 새로이 공부하면서 풀었다.
'''

# 2. 18111번 마인크래프트
import sys
input = sys.stdin.readline
n, m, b =map(int, input().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

height = 0
res = 1000000000000000000000000000

for k in range(257):
    mini = 0
    maxi = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] < k :
                mini += (k - mat[i][j])
            else:
                maxi += (mat[i][j] - k)
    inven = maxi + b
    if inven < mini:
        continue
    time = 2*maxi + mini
    if time <= res:
        res = time
        height = k
print(res, height)