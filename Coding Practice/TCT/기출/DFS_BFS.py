# 15 특정 거리의 도시 찾기
from collections import deque
n, m, k, x =map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int ,input().split())
    graph[a].append(b)

print(graph)