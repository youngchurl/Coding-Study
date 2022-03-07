# 1. 10773번 제로
import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = []
for i in range(n):
    num = int(input().rstrip())
    if num != 0:
        li.append(num)
    elif num == 0:
        li.pop()
print(sum(li))
