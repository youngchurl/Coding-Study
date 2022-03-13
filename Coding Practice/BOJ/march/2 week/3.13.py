# 이코테 3-3 숫자 카드 게임
# n, k = map(int, input().split())
# card = [list(map(int, input().split())) for _ in range(n)]
# res = 0
# for i in range(n):
#     if min(card[i]) > res:
#         res = min(card[i])
# print(res)
'''
리뷰: min을 사용할까 2중 for문을 쓸까 고민하다가 쉽게쉽게 가려고
min을 사용해서 풀었다!
'''

# 이코테 3-4 1이 될 때까지
# n, k = map(int, input().split())
# cnt = 0
# while n !=1:
#     if n%k == 0:
#         n //=k
#         cnt +=1
#     else:
#         n -=1
#         cnt +=1
# print(cnt)    
'''
리뷰 : 그리디 문제를 주구장창 풀다가 푸니깐 쉽게 느껴지는 문제 였다.
'''

# 이코테 4-1 상하좌우
# n = int(input())
# order = list(map(str, input().split()))
# od = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
# lo = [1,1]
# for i in order:
#     lo[0] +=od[i][0]
#     lo[1] +=od[i][1]
#     if lo[0] < 1 or lo[0] > n:
#         lo[0] -=od[i][0]
#     if lo[1] < 1 or lo[1] > n:
#         lo[1] -=od[i][1]
    
# print(lo)

'''
리뷰 : 좌표 설정해서 푸는법도 익숙해져야 하는데 아직까지는 이렇게 푸는게
더 익숙해서 선호하게 되는거 같다.
다음에는 다른 방법으로도 풀 수 있도록 노력해야지
'''

# 이코테 4-2 시각
# time = int(input())
# h = 0
# m = 0
# s = 0
# cnt = 0
# while True:
#     s +=1
#     if s == 60:
#         s %=60
#         m +=1
#     if m == 60:
#         m %=60
#         h +=1
#     if '3' in str(s) or '3' in str(m) or '3' in str(h):
#         cnt +=1
#     if h>time:
#         break
# print(cnt)

'''
리뷰 : 이렇게 풀어도 될지는 모르지만 문제를 직관적으로 접근했다.
'''

# 이코테 4장 실전문제 왕실의 나이트

al = 'abcdefgh'

order = input()
li = []
li.append(int(al.index(order[0])))
li.append(int(order[1])-1)
res = 0
# 좌표는 x,y 
di = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

for i in di:
    x = li[0]
    y = li[1]
    x +=i[0]
    y +=i[1]
    if not (x<0 or x>7 or y<0 or y >7):
        res +=1
print(res)