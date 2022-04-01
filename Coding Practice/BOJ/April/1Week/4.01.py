# 1.  2579번 계단오르기
# import sys
# input = sys.stdin.readline

# n = int(input())
# step = [int(input()) for _ in range(n)]

# d = [0]*(n+1)
# d[0] = step[0]
# d[1] = step[0]+step[1]
# d[2] = max(step[])

# 2. 1260번 DFS와 BFS
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [False]*(n+1)
res = []
def dfs(graph,s,res):
    res.append(s)
    d = [s]
    visit[s] = True
    while d:
        node = d.pop()
        for i in graph[node]:
            if visit[i] == False:
                visit[i] = True
                dfs(graph,i,res)
dfs(graph,v,res)
print(*res)
visit = [False]*(n+1)
res2 = []
def bfs(graph,s,res2):
    d = deque([s])
    visit[s] = True
    while d:
        node = d.popleft()
        res2.append(node)
        for i in graph[node]:
            if visit[i] == False:
                visit[i] = True
                d.append(i)
bfs(graph,v,res2)
print(*res2)