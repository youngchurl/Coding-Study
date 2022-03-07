# 1. 백준 11866번 요세푸스 문제 0

n, k = map(int, input().split())
k -=1
li = [i for i in range(1,n+1)]
res = []
while len(res)!=n:
    for i in range(k):
        if res.count(li[i]) == 0:
            li.append(li[i])
    res.append(str(li[k]))
    li = li[k+1:]
txt = ", ".join(res)
print(f'<{txt}>')

'''
리뷰 : 스터디에서 한번 숙제로 해봤고 못풀었는데 이번엔 이렇게 풀려서 기분이 굉장히
좋았고 무엇보다 풀이 방식을 까먹어서 새로 만든 방식임에도 풀려서 더 뿌듯하다! 
'''

# 2. 백준 10816번 숫자 카드 2
# 첫번째 풀이 : 시간초과
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

for i in li2:
    num = li.count(i)
    print(f'{num}',end=' ')

# 두번째 풀이 
import sys
input = sys.stdin.readline
n = int(input())
li = input().split()
dic = {i:0 for i in li}
for i in li:
    dic[i] +=1
m = int(input())
li2 = input().split()

for i in li2:
    if i in dic:
        num = dic[i]
    else:
        num = 0
    print(f'{num}',end=' ')

'''
리뷰 : 딕셔너리가 해쉬구조라 더 빠르겠거니 하고 생각해서 딕셔너리로 풀어봤는데
 다행히 풀렸다. 보통 리스트로 푸는데에 너무 익숙해졌는데, 앞으로 딕셔너리도 자주
 사용해봐야겠다.
'''

# 3. 백준 10816번 숫자 카드 2
import sys
input = sys.stdin.readline

a, b =map(int, input().split())
max_num = 0
for i in range(1,a+b):
    if a % i == 0 and b %i == 0 :
        max_num = i
tem1 = int(a/max_num)
tem2 = int(b/max_num)
print(max_num)
if tem1 <= tem2:
    print(b*tem1)
else:
    print(a*tem2)

'''
리뷰 : 그렇게 어려운 점은 없었지만 최소 공배수를 대략 10분이상은 고민했다...
'''
# 4. 백준 2164번 카드 2
import sys
input = sys.stdin.readline

n = int(input())
txt = ''
for i in range(1,n+1):
    txt +=str(i)

while True:
    txt = txt[1:]
    if len(txt) ==1:
        break
    txt +=txt[0]
    txt = txt[1:]
    if len(txt) ==1:
        break

print(txt)

# 다른 풀이

import sys
from collections import deque
input = sys.stdin.readline
li = [i for i in range(1,int(input())+1)]
deq = deque(li)

while len(deq) !=1:
    deq.popleft()
    deq.append(deq[0])
    deq.popleft()
print(*deq)

'''
리뷰 : 풀이자체는 안어려웠는데 시간초과랑 런타임에러때매 고생을 했다...
총 세번 문제를 풀었는데 1. 덱을 이용해서 2. 리스트를 이용해서 
3. 그냥 텍스트 슬라이싱을 이용해서 이중 1번을 제외하고 2,3은 모두 시간초과가 나왔다.
'''
# 5. 백준 1920번 수 찾기
import sys
input = sys.stdin.readline
n = int(input())
li = input().split()
m = int(input())
li2 = input().split()
dic = {i:0 for i in li}

for i in li2:
    if i in dic:
        print('1')
    else:
        print('0')

'''
리뷰 : 난이도는 쉬운데 시간초과가 계속 나와서 고민하다가 아까 딕셔너리로
풀었던게 생각나서 바로 적용했더니 정답이 나왔다!
'''

# 6. 백준 1259번 팰린드롬수
import sys
input = sys.stdin.readline
while True:
    txt = input().rstrip()

    if txt == '0':
        break

    txt2 = txt[::-1]

    n = len(txt)
    check = True

    for i in range(n):
        if txt[i] != txt2[i]:
            check = False
            break

    if check == True:
        print('yes')
    else:
        print('no')

'''
리뷰 : 근래 문제들이 다 그렇듯 이것도 에러때매 고생은 했지만 문제자체는 간단했다.
'''

# 7. 백준 1018번 체스판 다시 칠하기
import sys
input = sys.stdin.readline

col, row =map(int, input().split())
w = 'WB'*(row+col)
b = 'BW'*(row+col)

mat = [input().rstrip() for _ in range(col)]

case = 0
case2 = 0
if col == 8 and row == 8:
    for i in range(col):
        for j in range(row):
            if i%2 == 0:
                if mat[i][j] != w[j]:
                    case +=1
                if mat[i][j] != b[j]:
                    case2 +=1
            if i%2 == 1:
                if mat[i][j] != b[j]:
                    case +=1
                if mat[i][j] != w[j]:
                    case2 +=1
    if case <= case2:
        print(case)
    else:
        print(case2)
else:
    d = col - 8
    r = row - 8
    tem = []
    tem2 = 0
    for y in range(d+1):
        for x in range(r+1):           
            for i in range(8):
                for j in range(8):
                    if i%2 == 0:
                        if mat[i+y][j+x] != w[j]:
                            case +=1
                        if mat[i+y][j+x] != b[j]:
                            case2 +=1
                    elif i%2 == 1:
                        if mat[i+y][j+x] != b[j]:
                            case +=1
                        if mat[i+y][j+x] != w[j]:
                            case2 +=1
            tem.append(case)
            tem.append(case2)
            case = 0
            case2 = 0
    min_tem =min(tem)
    print(min_tem)

'''
리뷰 : 정말 너무 힘들었다... 구현은 간단한데 case 초기화를 까먹어서 왜이렇게
안되는건지 고민을 정말 오래했고 약 한시간동안 푼거같다... 다행히도 풀긴했지만 
만약에 여기에 더해서 시간제한도 있었다면 못 풀었을 것이다....
'''
