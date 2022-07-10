# 24416 알고리즘 수업
'''import sys
input = sys.stdin.readline
def fib(n):
    cnt1 = 0
    if n==1 or n==2:
        cnt1 +=1
        return cnt1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
# d = [0]*(n+1)
# d[1], d[2] = 1,1
# for i in range(3, n+1):
#     d[i] = d[i-1]+d[i-2]

print(fib(n),n-2)'''

# 2477 참외밭
'''
동쪽 : 1
서쪽 : 2
남쪽 : 3
북쪽 : 4
'''

d = [0,0,0,0,0]

k = int(input())
for _ in range(6):
    di, m =map(int, input().split())
    