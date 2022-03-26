# 1. Boj 3079번 입국심사
# import sys
# n, m = map(int, sys.stdin.readline().strip().split())
# li = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# li.sort()

# l = 1
# r = li[-1]*m

# while l<=r:
#     cnt = 0
#     mid = (l+r)//2
#     for i in li:
#         cnt += mid//i
#     if m <= cnt:
#         r = mid-1
#     else:
#         l = mid+1
# print(l)

'''
리뷰 : 슬슬 이분탐색도 단순하게 값을 서치하는게 아니라 그 숫자를 응용해서 풀어야하는
문제들이 생겨서 한문제 한문제가 어렵고 생각할게 많아지는게 체감이 된다...
'''
# 2. Boj 3649번 로봇 프로젝트
# import sys
# while True:
#     try:
#         x = int(sys.stdin.readline().rstrip())
#         n = int(sys.stdin.readline().rstrip())
#         li = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

#         li.sort()
#         x = int(x*10e6)
#         l = 0
#         r = n-1
#         flag = True
#         while l < r:
#             res = li[l] + li[r]
#             if res == x:
#                 flag = False
#                 break
#             if res < x:
#                 l +=1
#             elif res > x:
#                 r -=1
            
#         if flag:
#             print('danger')
#         else:
#             print(f'yes {li[l]} {li[r]}')
#     except:
#         break

'''
리뷰 : 여러 테스트 케이스가 있다고 나와 있기는 했었지만 나와있는 테스트 케이스가
없어서 무시했더니 문제가 안풀렸다...
그래서 혹시나 하는 생각에 질문게시판을 가보니 try except를 이용해야 한다고
써있었고 그걸 보고 바로 풀 수 있었다.
'''
# 3. Boj 15649번 N과 M (1)
# from itertools import permutations
# n, m = map(int, input().split())
# li = [i for i in range(1,n+1)]
# co = list(permutations(li, m))
# for i in co:
#     print(*i)

# 4. Boj 15650번 N과 M (2)
# from itertools import combinations
# n, m = map(int, input().split())
# li = [i for i in range(1,n+1)]
# co = list(combinations(li, m))
# for i in co:
#     print(*i)

# 5. Boj 15651번 N과 M (3)
# from itertools import *
# n, m = map(int, input().split())
# li = [i for i in range(1,n+1)]
# res = list(product(li, repeat = m))
# for i in res:
#     print(*i)

# 6. Boj 15652번 N과 M (4)

# from itertools import *
# n, m = map(int, input().split())
# li = [i for i in range(1,n+1)]
# res = list(combinations_with_replacement(li, m))
# for i in res:
#     print(*i)

'''
리뷰 : 네 개 문제 모두 라이브러리를 이용해 수월하게 풀 수 있었다.
'''
# 7. Boj 1904번 01타일 - DP
# n = int(input())
# d = [0]*(n+2)
# d[1] = 1
# d[2] = 2
# if n>=3:
#     for i in range(3,n+1):
#         d[i] = (d[i-1] + d[i-2])%15746

# print(d[n])

'''
리뷰 : 계속해서 메모리 초과가 뜨길래 어떤 이유인가 고민했는데... int가 계속해서 커지는데
리스트에 계속 큰값을 담아가니깐 메모리 초과가 뜬거였다! 문제를 잘읽고 나머지 조건이 있다면
잘 체크해봐야겠다!
'''

# 8. Boj 9461번 파도반 수열
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     d = [0]*(n+3)
#     d[1] = 1
#     d[2] = 1
#     d[3] = 1
#     for i in range(4, n+1):
#         d[i] = d[i-2] + d[i-3]
#     print(d[n])

'''
리뷰 : DP 공부를 하면서 index에러와 가장 많이 부딪힌 문제 같은데 앞으로 d 공간 확보할때는
i-n 될때 n 만큼을 해야된다는 교훈을 얻을 수 있었다.
'''

# 9. Boj 12865번 평범한 배낭
n, k =map(int, input().split())
li = [list(map(int, input().split())) for _ in n]
