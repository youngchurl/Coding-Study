# 1. 10773번 제로
"""
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
"""
'''
리뷰 : 생각한대로 풀었고, 또 맞았다!
'''

# 백준 1654번 랜선자르기
n, k = map(int, input().split())
li = []
for _ in range(n):
    li.append(int(input()))
li2 = []
res = 0
i = 1 
while True:
    li.sort()
    li[0]//i
    

print(i)