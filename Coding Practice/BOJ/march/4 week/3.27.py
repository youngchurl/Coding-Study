# 1. Boj 1931번 회의실 배정
# import sys
# input = sys.stdin.readline
# n = int(input())
# li = []
# for _ in range(n):
#     a, b =map(int, input().rstrip().split())
#     li.append([b,a])
# li.sort()
# res = 0
# cnt = 0
# for i in li:
#     if res<=i[1]:
#         res = i[0]
#         cnt += 1
# print(cnt)

'''
리뷰 : 처음 그리디 공부하면서 회의실 문제를 보고 엄청 고민했던게 떠오르는데
확실히 문제 풀면서 실력이 늘은건지 어떻게 풀어야겠다는 생각을 바로 할 수 있었다.
'''
