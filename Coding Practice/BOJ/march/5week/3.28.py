# 1. 2630번 색종이 만들기
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
res = []

def cut(x,y,n):
    color = mat[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != mat[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if color == 1:
        res.append(1)
    else:
        res.append(0)
cut(0,0,n)
print(res.count(0))
print(res.count(1))