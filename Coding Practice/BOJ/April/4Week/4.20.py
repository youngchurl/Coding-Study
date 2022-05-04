# 1300번 K번째 수
'''n = int(input())
b = int(input())
li = [[0]*n for _ in range(n)]
b_li = []
for i in range(n):
    for j in range(n):
        li[i][j] = (i+1) * (j+1)
        b_li.append(li[i][j])
b_li.sort()
print(b_li[b])'''
# 메모리 초과

n = int(input())
k = int(input())
