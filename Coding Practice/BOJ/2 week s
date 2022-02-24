2022.01.28

# 2577번 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

total = str(a*b*c) # 곱셈한 값을 문자 형태로 변환시킨다.
li = [] # 빈 리스트 생성

for i in range(len(total)):
    li.append(total[i]) # 문자열 각요소를 리스트에 담는다.

for j in range(10):
    print(li.count(str(j))) # 각 숫자가 몇 개 있는지 일렬로 출력

# 8958번 OX퀴즈

T = int(input()) # 테스트 케이스 입력

for _ in range(T):
    test = input() # 문자형으로 OX 데이터를 받는다.
    cnt = 0 # O의 숫자를 세는 역할,  일단 0 으로 초기화
    res = 0 # cnt값을 더할때 쓸값,  일단 0 으로 초기화

    for i in range(len(test)):
        if test[i] == 'O':
            cnt += 1 # 문자가 O 일경우 cnt를 1씩 증가 시킨다.
            res += cnt # 증가시킨 cnt를 res에 합산한다.
        else:
            cnt = 0 # X 가 나왔으므로 cnt 초기화
    print(res) # 총 더한 값을 출력한다.


# 10828번 스택

import sys
num = int(sys.stdin.readline()) # 반복 횟수
li = [] # 스택을 넣어둘 리스트

for _ in range(num):

    order = sys.stdin.readline().split() # 명령 입력 

# push 명령
    if 'push' in order:
        li.append(order[1]) # 처음에 단순하게 order[-1]로 해서 틀림

# pop 명령
    elif 'pop' in order: 
        if len(li) == 0:
            print('-1')
        else:
            print(li[-1])
            li.pop(-1)
    
# size 명령
    elif 'size' in order: 
        print(len(li))

# empty 명령    
    elif 'empty' in order:
        if len(li) == 0:
            print('1')
        else:
            print("0")

# top 명령
    elif 'top' in order :
        if len(li) == 0:
            print('-1')
        else:
            print(li[-1])

# 시간초과 때문에 input -> sys.stdin.readline() 사용
