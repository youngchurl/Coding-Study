# 1. 2606번 바이러스
from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
dic = {}
for i in range(n):
    dic[i+1] = set()
for _ in range(m):
    a,b =map(int, sys.stdin.readline().rstrip().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    d = deque([start])
    while d:
        for i in dic[d.popleft()]:
            if i not in visit:
                visit.append(i)
                d.append(i)
visit = []
bfs(1,dic)
print(len(visit)-1)


# 2. 1260번 DFS와 BFS
from collections import deque
import sys
n, m, s = map(int, sys.stdin.readline().rstrip().split())
dic = {}
for i in range(n):
    dic[i+1] = set()

for j in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    visit = []
    d = deque()

    d.append(start)

    while d:
        node = d.popleft()
        if node not in visit:
            visit.append(node)
            d.extend(dic[node])
    return visit

def dfs(start, dic):
    visit = []
    q = []

    q.append(start)

    while q:
        node = q.pop()
        if node not in visit:
            visit.append(node)
            q.extend(dic[node])
    return visit

print(dfs(s, dic))
print(bfs(s, dic))