# 1932번 정수 삼각형
import copy
n = int(input())
li = []
li.append(int(input()))
for _ in range(n-1):
    li.append(map(int, input().split()))
mat = copy.deepcopy(li)

for i in range(n):
    for j in range(n-len(li[i])):
        mat.append(0)
print(mat)