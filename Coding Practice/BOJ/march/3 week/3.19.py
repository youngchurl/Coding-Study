# 1. Boj 1260번 DFS 와 BFS
# from collections import deque
# n, m, v = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# visit = [False] * (n+1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     graph[a].sort()
#     graph[b].sort()

# def dfs(graph, v, visit):
#     visit[v] = True
#     print(v, end=' ')
    
#     for i in graph[n]:
#         if not visit[i]:
#             dfs(graph, i, visit)

# def bfs(graph, v, visit):
#     visit = [False] * (n + 1)
#     d = deque([v])
#     visit[v] = True

#     while d:
#         node = d.popleft()
#         print(node, end = ' ')
#         for i in graph[node]:
#             if not visit[i]:
#                 d.append(i)
#                 visit[i] = True

# dfs(graph, v, visit)
# print()
# bfs(graph, v, visit)

# 2. Boj 10815번 숫자 카드
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))
li.sort()
mark = [0] * m

for i in range(m):
    s = 0
    e = n-1
    while s<=e:
        mid = (s+e)//2
        
        if li[mid] <li2[i]:
            s = mid+1
        elif li[mid] >li2[i]:
            e = mid-1
        if li[mid] == li2[i]:
            mark[i] = 1
            break
print(*mark)