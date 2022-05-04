# 1916번 최소 비용 구하기
n = int(input())
m = int(input())
bus = []
for _ in range(m):
    a,b,c = map(int, input().split())
    bus.append([a,b,c])
s,e = map(int ,input().split())

res = 1e7
for i in bus:
    if i[0] == s:
        if i[1] == e:
            res = min(res,)