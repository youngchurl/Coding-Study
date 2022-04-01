# 1. 6236번 용돈관리
# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())

# money = [int(input()) for _ in range(n)]

# l = 1
# r = sum(money)

# while l<=r:
#     mid = (l+r)//2
#     cnt = 0
#     tem = 0
#     flag = False
#     for i in money:
#         if tem <i:
#             if mid >=i:
#                 tem = 0
#                 tem +=mid
#                 tem -=i
#                 cnt +=1
#             else:
#                 flag = True
#         else:
#             tem -=i

#     if cnt>m or flag==True:
#         l = mid+1
#     else:
#         r = mid-1
# print(l)

'''
리뷰: 하루에 주어진 금액이 부족한 경우를 생각하지 못해서 힘들었지만,
 생각하고나서는 바로 풀 수 있었다.
'''

# 2. 2748번 피보나치 2
n = int(input())
d = [0]*(n+1)
d[1] = 1

for i in range(2,n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])

'''
리뷰: 기본 동적 프로그래밍!
'''

# 3. 11053번 가장 긴 증가하는 부분
# n = int(input())
# li = list(map(int, input().split()))
# li = list(set(li))
# li.sort()
# print(len(li))
