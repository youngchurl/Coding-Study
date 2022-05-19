n = int(input())
mat = [[0]*n for _ in range(n)]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] == 1:
            mat[i][j] = 1

print(mat)

for i in range(n):
    for j in range(n):
        if mat[i][j] ==1:
            mat[j][]