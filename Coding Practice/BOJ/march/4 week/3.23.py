# 1. Boj 11726번 2Xn 타일

'''
1:1
2:2
3:1+2 , 3
4:1+1+3 , 5
'''
# n = int(input())
# d = [0]*1001
# d[0],d[1],d[2]=0,1,2
# for i in range(3,n+1):
#     d[i] = d[i-2]+d[i-1]
# print(d[n]%10007)
'''
문제 유형 : DP
리뷰 : DP는 아직도 익숙하지 않아 불안했지만 다행히 맞았다!
'''

# 2. Boj 1149번 RGB거리
'''
r - gb - br
g - br - rb
b - gr - rg
총 여섯개의 경우의 수가 주어진다.
우선적으로 같은 색을 칠하는 집끼리 합친다.
'''
# import sys
# from itertools import permutations
# n = int(sys.stdin.readline().rstrip())
# h1 = [0]*3
# h2 = [0]*3
# h3 = [0]*3

# for i in range(n):
#     r, g ,b=map(int, sys.stdin.readline().rstrip().split())
#     if i%3 == 0:
#         h1[0]+=r 
#         h1[1]+=g
#         h1[2]+=b
#     if i%3 == 1:
#         h2[0]+=r 
#         h2[1]+=g
#         h2[2]+=b
#     if i%3 == 2:
#         h3[0]+=r 
#         h3[1]+=g
#         h3[2]+=b
# res = []
# pr = list(permutations([0,1,2],3))
# print(pr)
# for i in pr:
#     tem = h1[i[0]]+h2[i[1]]+h3[i[2]]
#     res.append(tem)
# print(res)
# print(min(res))

# 두번째 풀이
# import sys
# n = int(sys.stdin.readline())
# d = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# for i in range(1,n):
#     d[i][0] = min(d[i-1][1],d[i-1][2]) + d[i][0]
#     d[i][1] = min(d[i-1][0], d[i-1][2]) + d[i][1]
#     d[i][2] = min(d[i-1][0], d[i-1][1]) + d[i][2]
# print(min(d[n-1][0], d[n-1][1], d[n-1][2]))

'''
리뷰 : 문제 이해가 제대로 안되기도 했는데 안봤다면 못풀꺼같았다..
DP 는 계속해서 봐야겠다.
'''

# 2. Boj 11727번 2xn 타일링 2
'''
1: 1
2: 3 
3:1+2 5
4:1+3, 2, 3+1 1+1+2, 2+2 9 
5: 1,4 2,3 3,2 4,1 = 10 8 = 18
6: 
'''
# n = int(input())
# d = [0]*(n+1)
# d[1], d[2],d[3] = 1,3,5
# for i in range(4,n+1):
#     if i%2 == 0:
#         d[i] = d[i-1] + d[i-3] + d[1]
#     else:
#         d[i] = d[i]

# print(d[n])

# 3. Boj 2751번 수 정렬하기 2
# import sys
# from collections import deque
# tc = int(sys.stdin.readline().rstrip())
# li = deque([int(sys.stdin.readline().rstrip()) for _ in range(tc)])
# li = sorted(li)
# for i in li:
#     print(i)
    
'''
리뷰 : 음 틀림으로 되서 풀어봤는데 sort로 풀려서 놀랐다.
'''

# 4. Boj 18870번 좌표 압축
n = int(input())
li = list(map(int, input().split()))
se = set(li)