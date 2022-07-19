# 1080번 행렬
n,m = map(int, input().split())

li1 = [input() for _ in range(n)]
li2 = [input() for _ in range(n)]
mat1 = [[]*n]
mat2 = [[]*n]

for i in range(n):
    for j in li1[i]:
        mat1[i].append(j)

for i in range(n):
    for j in li2[i]:
        mat2[i].append(j)

print(mat1)
print(mat2)
cnt = 0

if n <3 or m<3:
    print(-1)
else:
    for j in range(n-2):
        for i in range(m-2):
            if mat1[i][j] != mat2[i][j]:
                cnt +=1
                for k in range(3):
                    for r in range(3):
                        if (i+k<=n) and (j+r<=m):
                            if mat1[i+k][j+r] == '1':
                                mat1[i+k][j+r] = '0'
                            else:
                                mat1[i+k][j+r] = '1'
    print(cnt)

'''
1. 

'''