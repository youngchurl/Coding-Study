
백준 1927번 최소힙

import sys
import heapq

heap = []

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    
    if n == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap))
    elif n > 0:
        heapq.heappush(heap, n)

2022.02.16

백준 1874 스택수열
import sys
input = sys.stdin.readline
li = []
res = []
cnt = 1
err = True
t = int(input())
for i in range(t):
    a = int(input())
    
    while a >= cnt:
        li.append(cnt)
        res.append("+")
        cnt +=1

    if a == li[-1]:
        li.pop()
        res.append("-")
    
    else:
        err = False
if err == False:
    print("NO")
else:
    print("\n".join(res))

1158번 요세푸스 문제

a,b = map(int, input().split())
i = 0
cnt = b -1
err = False
li = [i for i in range(1,a+1)]
res = []

while len(res) != a:
    if li[cnt] not in res:
        res.append(li[cnt])
        cnt += b
        if cnt >= a:
            cnt %= a
    elif li[cnt] in res:
        cnt +=1
print(res)
