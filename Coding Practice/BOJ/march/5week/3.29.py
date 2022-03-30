# 1. 2512번 예산
# n = int(input())
# li = list(map(int ,input().split()))
# m = int(input())

# l = 1
# r = m
# re = sum(li)
# while l<=r:
#     mid = (l+r)//2
#     res = 0
#     for i in li:
#         if i<mid:
#             res += i
#         else:
#             res += mid

#     if res<=m:
#         l = mid +1
#     else:
#         r = mid -1
# if re <= m:
#     print(max(li))
# else:
#     print(r)

'''
리뷰 : 이제 이분탐색은 어느정도 익숙해졌다!
'''

# 2. 1072번 게임
import math
x,y = map(int, input().split())
wr = math.trunc((y*100/x))
res = wr+1
l = 1
r = 20000000000
if wr >=99:
    print(-1)
else:
    while l<=r:
        mid = (l+r)//2
        game = x+mid
        win = (y+mid)
        winrate = math.trunc((win*100/game))

        if res > winrate:
            l = mid + 1
        else:
            r = mid - 1
    print(l)

'''
리뷰 : 확률이 99퍼 이상일때를 고려해야하는 점을 간과했었고
math.trunc를 이용해서 소숫점을 제거해야된다는걸 처음으로 알 수 있었다.
그리고 실수부 계산이 이상해질 수 있으니 먼저 100을 곱한다음에 나누는게
더 정확한 값을 도출할 수 있다는 점을 배웠다.
'''