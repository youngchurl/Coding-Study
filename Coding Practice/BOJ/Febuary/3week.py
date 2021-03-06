# 2022.02.02
# 백준 1157 단어공부

from collections import Counter

li_text = [i for i in input().upper()] # 문자를 리스트로 입력받는다.
most = Counter(li_text).most_common(2) # 최빈값 두개를 비교하기 위해 부름
if most[0][1] == most[1][1]: # 최빈값이 겹치는지 비교
    print("?")
else:
    print(f'{most[0][0]}') # 최빈값 출력


# 2022.02.04

# 백준 1316번 그룹단어 체커
# 실패
num = int(input()) # 단어 입력 개수
res = num # 그룹단어 갯수를 우선 단어 갯수로 둔다.

for _ in range(num):
    txt = input()
    li_txt = [] 


    for i in range(len(txt)-1):
        if txt[i] != txt[i+1]:
            
            # 리스트안에 텍스트가 있다면 그룹단어가 아니기 때문에 res -1 
            if txt[i] in li_txt:
                res -=1

            # 텍스트 리스트안에 텍스트가 없다면 입력
            else:
                li_txt.append(txt[i])
print(res)


# 정답
a = int(input())

to = 0

for i in range(a):
    word = input()
    e = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new = word[j+1:]
            if new.count(word[j])> 0 : 
                e +=1
    if e == 0:
        to +=1
print(to)

# 10866번 덱
from collections import deque
import sys

input = sys.stdin.readline # 길어서 input으로 정의해놓고 시작
deq = deque() # 덱을 deq로 지정

for _ in range(int(input())):
    order = input().split()
    if 'push_front' in order:
        deq.appendleft(order[1])

    elif 'push_back' in order:
        deq.append(order[1])

    elif 'pop_front' in order:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
            deq.popleft()

    elif 'pop_back' in order:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])
            deq.pop()

    elif 'size' in order:
        print(len(deq))
    
    elif 'empty' in order:
        if len(deq) == 0:
            print("1")
        else:
            print("0")

    elif 'front' in order:
        if len(deq) == 0:
            print('-1')
        else:
            print(deq[0])

    elif 'back' in order:
        if len(deq) == 0:
            print('-1')
        else:
            print(deq[-1])
            
            
            
# 2022.02.08

# BOJ 9013번 괄호

T = int(input())
for _ in range(T):
    txt = [i for i in input()]
    cl = 0
    cr = 0
    err = 0
    for i in range(len(txt)):
        if txt[i] == "(":
            cl +=1
        elif txt[i] == ")":
            cr +=1
        if cl < cr :
            err +=1
            break
    if err == 0 and cl == cr:
        print("YES")
        
    else:
        print("NO")
    
