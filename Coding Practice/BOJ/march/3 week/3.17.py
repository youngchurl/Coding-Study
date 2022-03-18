# 1.Boj 1463번 1로 만들기 
'''
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
0, 0, 1, 1
'''
n = int(input())

d = [0,0,1,1]
if n <4:
    print(d[n])
else:
    for i in range(4, n+1):
        d.append(d[i-1]+1)
        if i%2 == 0:
            d[i] = min(d[i//2]+1, d[i])
        if i%3 == 0:
            d[i] = min(d[i//3]+1, d[i])
    print(d[n])

'''
리뷰 : 아직 DP 가 익숙하지 않음을 알 수 있는 문제였다. 더 열심히 DP 부분을 봐둬야 될것같다.
'''

# 2. Boj 9095번 1,2,3 더하기

'''
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
[1], [1,1], [2], [1,1,1], [2,1],[1,2], [3]
[1,2,4]
'''
tc = int(input())
for i in range(tc):
    n = int(input())
    dp = [0,1,2,4]
    for j in range(4,n+1):
        dp.append(0)
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[n])

'''
리뷰 : DP 연습겸 1로 만들기랑 같이 있는 문제라 풀엇는데 잘풀려서 기분이 좋았다.
'''

# 3. Boj 2579번 계단 오르기
import sys
input = sys.stdin.readline
n = int(input())
li = [int(input().rstrip()) for _ in range(n)]
cnt =1
le = len(li) - 1
li[::-1]
res = li[0]
i = 1
while True:
    if i == le-1 and cnt ==2:
        break
    elif i == le-1 and cnt !=2:
        res +=li[i]
        break
    elif i == le:
        break
    if li[i+1]> li[i] or cnt ==2:
        res +=li[i+1]
        i += 2
        cnt = 1
    else:
        res +=li[i]
        i += 1
        cnt ==2
print(res)