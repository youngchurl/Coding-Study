# 백준 1966번 프린터 큐
# import sys
# input = sys.stdin.readline
# tc = int(input().rstrip())

# for _ in range(tc):
#     a, b = map(int, input().split())
#     txt = list(map(int, input().split()))
#     tem = txt[b]
#     txt2 = txt[::-1] # 거꾸로
#     cnt1 = 0 # 보다 큰 수
#     cnt2 = 0 # 같은데 먼저 출력되는 수
#     flag = 0

#     for i in range(a):
#         if txt[i] > tem:
#             cnt1 +=1
#             flag = i
#     if cnt1 >=1 and b !=0:
#         cnt2 +=1
#         for j in range(b):
#             if txt[j] == tem:
#                 cnt2 +=1
#         for k in range(a-flag):
#             if txt2[k] == tem:
#                 cnt2 +=1     

#     elif cnt1 >=1 and b == 0:
#         cnt2 +=1
#         for k in range(a-flag):
#             if txt2[k] == tem:
#                 cnt2 +=1     
#     res = cnt1 + cnt2
#     if a == 1:
#         print('1')
#     else:
#         print(res)

# 두 번째 풀이

from collections import deque
tc = int(input())

