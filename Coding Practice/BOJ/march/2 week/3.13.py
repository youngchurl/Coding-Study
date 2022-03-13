# 백준 18111번 마인크래프트
n, m, b = map(int, input().split())
mat = [[map(int, input().split())] for _ in range(n)]
li = []

for i in range(n):
    for j in range(m):
        li.append(mat[i][j])

li.sort()
li2 = li