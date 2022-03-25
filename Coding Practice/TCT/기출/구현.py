# 7. 럭키 스트레이트
# txt = input()
# le = len(txt)
# mid = le//2
# l = [int(i) for i in txt[:mid]]
# r = [int(i) for i in txt[mid:]]
# if sum(l) == sum(r):
#     print('LUCKY')
# else:
#     print('READY')

'''
리뷰 : 다 풀고보니 중간과정 리스트 만드는걸 생략하고 애초에 리스트로
받아서 문제를 풀어도 괜찮았을것 같다.
'''

# txt = [int(i) for i in input()]
# mid = len(txt)//2
# if sum(txt[:mid]) == sum(txt[mid:]):print('LUCKY')
# else: print('READY')

'''
리뷰 : 위의 풀이를 리스트로 새롭게 풀어봤다.
'''

# 8. 문자열 재정렬
# inp = input()
# num = [int(i) for i in inp if i in '0123456789']
# txt = [i for i in inp if not i in '0123456789']
# txt.sort()
# txt.append(str(sum(num)))
# print(''.join(txt))

'''
리뷰 : 직관적으로 풀었다.
'''

# 9. 문자열 압축

# def solution(s):
#     answer = 0
#     le = len(s)
#     cnt = 0
#     res = [le]
#     while cnt != le:
#         tem = []
#         tem2 = []
#         cnt +=1

#         n = 0
#         txt = ''
#         for i in s:
#             n +=1
#             txt +=i
#             if n == cnt:
#                 n = 0
#                 tem.append(txt)
#                 txt =''
#         tem.append(txt)

#         s2 = s[::-1]
#         n = 0
#         txt = ''
#         for i in s2:
#             n +=1
#             txt +=i
#             if n == cnt:
#                 n = 0
#                 tem2.append(txt)
#                 txt =''
#         tem2.append(txt)

#         le2 = len(tem)
#         resn = 0
#         re = le

#         for j in range(le2-1):
#             if tem[j] == tem[j+1]:
#                 resn +=1
#                 re -=cnt
#             else:
#                 print(re)
#                 re +=1
#                 resn = 0
        
#         if re != 0:
#             res.append(re)
#         if le % 2 == 0:
#             le2 = len(tem)
#             resn = 0
#             re = le

#             for j in range(le2-1):
#                 if tem2[j] == tem2[j+1]:
#                     resn +=1
#                     re -=cnt
#                 else:
#                     if resn >0:
#                         re +=1
#                     resn = 0
            
#             if re != 0:
#                 res.append(re)
#     answer = min(res)
#     return answer

'''
정확성 : 48점
'''

# 11. 뱀 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
mat = [[0]*(n+1) for _ in range(n+1)]
di =[(0,1), (1,0), (0,-1), (-1,0)] # 방향
apple = int(input())

for _ in range(apple):
    a,b = map(int, input().split())
    mat[a+1][b+1] = 1

d = int(input())
direction = deque()

for _ in range(d):
    direction.append(list(map(str, input().rstrip().split())))

i = 0
st = [1,1]
t = 0
tail = deque()
crush = False

while True:
    # 꼬리 구현
    if tail:
        for j in range(len(tail)):
            if j == 0:
                tail[0] = st
            else:
                tail[j] = tail[j-1]

    st[0] += di[t][0]
    st[1] += di[t][1]

    # 사과 구현
    if st[0] <= 0 or st[0] >= n or st[1] <= 0 or st[1] >= n:
        if mat[st[0]][st[1]] == 1:
            mat[st[0]][st[1]] = 0
            tail.append([st[0],st[1]])

        else:
            if tail:
                tail.popleft()

    i +=1
    # 게임 종료 조건 구현 꼬리 x
    if st[0] <= 0 or st[0] >= n or st[1] <= 0 or st[1] >= n:
        break

    # 꼬리 건들때 게임 종료 조건 구현
    if tail:
        for k in tail:
            if k == st:
                crush = True

    if crush:
        break

    # 방향 변환 구현
    if direction:
        if str(i) == direction[0][0]:
            if direction[0][1] == 'D':
                t +=1
                t %=4

            else:
                t -=1
                if t == -4:
                    t = 0
            direction.popleft()

if st[0] <= 0 or st[0] >= n or st[1] <= 0 or st[1] >= n:
    print(i)
else:
    print(i+1)

'''
리뷰 : 예제는 풀리는데 런타임에러로 문제해결이 안된다.
'''

# 13 치킨배달
'''
0 : 빈칸, 1: 집, 2: 치킨집
'''

# n,m = map(int, input().split())
# mat = [list(map(int, input().split())) for _ in range(n)]
# home = []
# chi = []
# for i in range(n):
#     for j in range(n):
#         if mat[i][j] == 1:
#             home.append([i+1,j+1])
#         if mat[i][j] == 2:
#             chi.append([i+1,j+1])

# ch_st = []
# chi_li = [] 

# for i in range(len(chi)):
#     for j in range(len(home)):
#         ab = abs(home[j][0] - chi[i][0]) + abs(home[j][1] - chi[i][1])
#         chi_li.append(ab)
#     ch_st.append(chi_li)
#     chi_li = []
# home_st = list(map(list, zip(*ch_st)))

# le_home = len(home)
# le_chi = len(chi)

# res = 0
# if m ==le_chi:
#     for i in home_st:
#         res+=min(i)
#     print(res)
# else:
#     chsum = {}
#     for i in range(le_chi):
#         chsum.setdefault(sum(ch_st[i]), i)
#     chsum = sorted(chsum.items())
#     index = []
#     print(chsum)

#     if m ==1:
#         print(chsum[0][0])
#     else:
#         for i in range(m):
#             index.append(chsum[i][1])
        
#         new_home_st = []
#         for i in home_st:
#             tem = []
#             for j in index:
#                 tem.append(i[j])
#             new_home_st.append(tem)

#         print(new_home_st)

#         for i in new_home_st:
#             res +=min(i)
#         print(res)

# 두번째 풀이 조합사용
# from itertools import combinations
# n,m = map(int, input().split())
# mat = [list(map(int, input().split())) for _ in range(n)]
# home = []
# chi = []
# for i in range(n):
#     for j in range(n):
#         if mat[i][j] == 1:
#             home.append([i+1,j+1])
#         if mat[i][j] == 2:
#             chi.append((i+1,j+1))

# ch_st = []
# if m ==1:
#     for i in chi:
#         tem = []
#         for j in home:
#             ab = abs(i[0]-j[0]) + abs(i[1]-j[1])
#             tem.append(ab)
#         ch_st.append(tem)
        
#     res = [sum(i) for i in ch_st]
#     print(min(res))

# elif m == len(chi):
#     res = 0
#     for i in home:
#         tem = []
#         for j in chi:
#             ab = abs(i[0]-j[0]) + abs(i[1]-j[1])
#             tem.append(ab)
#         ch_st.append(tem)
#     for i in ch_st:
#         res +=min(i)
#     print(res)

# else:
# res = 0
# ch = list(combinations(chi, m))
# for i in home:
#     tem = []
#     for j in ch:
#         for k in j:
#             ab = abs(i[0]-k[0]) + abs(i[1]-k[1])
#             tem.append(ab)
#     ch_st.append(tem)

# for i in ch_st:
#     res +=min(i)
# print(res)

'''
from itertools import combinations
 
## 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
## 빈칸(0), 집(1), 치킨집(2)
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))
 
minv = float('inf')
for ch in combinations(chicken, M):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv: break
    if sumv < minv: minv = sumv
 
print(minv)


출처: https://juhee-maeng.tistory.com/96 [simPLE]
'''

