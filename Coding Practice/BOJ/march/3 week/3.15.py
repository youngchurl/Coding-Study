# 1. Boj 1966번 프린터 큐
from collections import deque
tc = int(input())
for _ in range(tc):
    n, m =map(int, input().split())
    d =deque(map(int, input().split()))
    
    t = d[m] # 타깃
    d[m] = 0
    cnt = 1
    if n == 1 :
        print('1')
    else:
        while True:
            if d[0] == 0:
                if max(d)<=t:
                    print(cnt)
                    break
                else:
                    d.append(d[0])
                    d.popleft()

            if d[0] == max(d) and d[0]>=t:
                d.popleft()
                cnt +=1
            else:
                d.append(d[0])
                d.popleft()
    
'''
리뷰 : 분명 로직이 간단하다고 생각하고 문제에 접근했는데 계속해서 틀려서
멘붕되고 문제 풀이 자체가 싫어지게 될뻔했는데 다행히도 오늘 푸는데 성공해서
뿌듯하다.
'''
# 2. Boj 2108번 통계학

from collections import Counter
import sys
input = sys.stdin.readline
num_li = []
for _ in range(int(input().rstrip())):
    num_li.append(int(input().rstrip()))

nsum = sum(num_li)
le = len(num_li) // 2
num_li.sort()

res1 = round(nsum/len(num_li))
if len(num_li) !=1:
    res2 = num_li[le]
else:
    res2 = num_li[0]

if len(num_li) !=1:
    res3 = Counter(num_li).most_common(2)
    if res3[0][1] == res3[1][1]:
        res3 = res3[1][0]
    else:
        res3 = res3[0][0]
else:
    res3 = num_li[0]

if len(num_li) !=1:
    res4 = num_li[-1] - num_li[0]
else:
    res4 = 0

print(res1)
print(res2)
print(res3)
print(res4)

'''
리뷰 : 시간초과랑 런타임 에러로 인해서 고생해서 하나하나 조건을 두고 문제를 풀었다.
'''

# 3. Boj 2805번 나무 자르기
'''import sys
input = sys.stdin.readline
n, m =map(int, input().split())
li = list(map(int, input().split()))

l, r =1,max(li)

while l <=r:
    mid = (l+r) //2

    log = 0
    for i in li:
        if i >= mid:
            log += i - mid
    if log >= m:
        l = mid +1
    else:
        r = mid -1
print(r)'''

'''
리뷰 : 이진탐색 부분이 약해서, 보완하고 싶은 맘에 세번 정도 풀어봤는데 마지막에서야
어느정도 이해가 되고 아직도 실용하려면 못할것 같다는 생각이 든다...
더 열심히 해야지!
'''

# 4. BOJ 4949번 균형잡힌 세상
while True:
    txt = input()
    if txt == '.':
        break
    new_txt = ''
    dic = {'(':0, '[':0, ')':0, ']':0}
    flag = True
    for i in txt:
        if i in '()[]':
            new_txt +=i
            dic[i] +=1
            if dic['('] < dic[')'] or dic['['] < dic[']']:
                flag = False
            if len(new_txt) >= 2:
                tem = new_txt[-2]
                if tem == '(' and i ==']':
                    flag = False
                if tem == '[' and i == ')':
                    flag = False

    if dic['('] != dic[')'] or dic['['] != dic[']']:
        flag = False

    if flag == False:
        print('no')
    else:
        print('yes')

'''
리뷰 : 여태까지 나온 반례는 다 맞았는데 왜 틀린지 알 수가없는 문제다....
'''

# BoJ 18111번 마인크래프트
from collections import deque
n,m,b = map(int, input().split())
mat = [list(map(str, input().split())) for _ in range(n)]
li = []
for i in range(n):
    for j in range(m):
        li.append(mat[i][j])
d = deque(li)
while True:
    