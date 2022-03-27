# 1. Boj 1931번 회의실 배정
import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    a, b =map(int, input().rstrip().split())
    li.append([b,a])
li.sort()
res = 0
cnt = 0
for i in li:
    if res<=i[1]:
        res = i[0]
        cnt += 1
print(cnt)