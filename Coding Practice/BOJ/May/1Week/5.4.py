# 15988번 1,2,3 더하기
# import sys
# input = sys.stdin.readline
# tc = int(input())
# li = []
# for _ in range(tc):
#     li.append(int(input()))
# n = max(li)
# d = [0]*(n+2)
# d[1]=1
# d[2]=2
# d[3]=4
# for i in range(4,n+1):
#     d[i] = (d[i-1]+d[i-2]+d[i-3])%1000000009
# for j in li:
#     print(d[j])

# 1912번 연속합

n = int(input())

li = list(map(int, input().split()))
res = [li[0]]
for i in range(n-1):
    res.append(max(res+li[i+1],li[i+1]))
print(max(res))