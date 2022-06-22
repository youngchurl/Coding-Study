# 9372번 상근이의 여행
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = [[] for _ in range(n+1)]
    res = 0
    i = 0
    for i in range(m):
        a, b = map(int, input().split())
        if not b in li[a]:
            li[a].append(b)
        if not a in li[b]:
            li[b].append(a)
    while res !=n:
        
