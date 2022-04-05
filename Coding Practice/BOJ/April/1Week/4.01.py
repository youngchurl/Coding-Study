# 1.  2579번 계단오르기
'''N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2] 

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])  

    print(dp[N])

'''

# 2. 2309번 일곱 난쟁이
from itertools import combinations
li = [int(input()) for _ in range(9)]
res = list(combinations(li,7))
for i in res:
    if sum(i) == 100:
        r = sorted(i)
        print(*r)
        exit()
