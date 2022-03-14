# SW 아카데미 1926번

import sys
input = sys.stdin.readline

num = int(input())

for i in range(1,num+1):
    j = str(i)
    cnt = 0
    if len(j)>=3: # 백의 자리 숫자일 경우
        if int(j[0]) % 3 == 0: # 백의 자리
            cnt +=1
        if int(j[1]) % 3 == 0 and int(j[1]) != 0: # 십의 자리
            cnt +=1
        if int(j[2]) % 3 == 0 and int(j[2]) != 0: # 일의 자리
            cnt +=1
        
        if cnt >= 1 : # 각각의 숫자가 3으로 나누어 떨어질때 cnt 가 늘어난다.
            print("-"*cnt, end=" ")
        else:
            print(j,end=" ")

    elif len(j)>=2: # 십의 자리 숫자일 경우
        if int(j[0]) % 3 == 0:
            cnt +=1
        if int(j[1]) % 3 == 0 and int(j[1]) != 0:
            cnt +=1
        
        if cnt >= 1 :
            print("-"*cnt, end=" ")
        else:
            print(j,end=" ")

    elif len(j)>=1: # 일의 자리 숫자일 경우
        if int(j[0]) % 3 == 0:
            cnt +=1
            
        if cnt >= 1 :
            print("-"*cnt, end=" ")
        else:
            print(j,end=" ")
한줄 평 : 처음에 10 같은 경우 0은 3으로 나눠도 나머지가 0임을 고려하지 못했었는데, 이 점을 고치고 나니 어려운 문제는 아니었다.


# 1206번 View

T = int(input())

for i in range(1,T+1):
    n = int(input())
    num = list(map(int, input().split()))
    res = []

    for j in range(2, n-2):
        if num[j] > num[j-1] and num[j] > num[j-2] and num[j] > num[j+1] and num[j] > num[j+2]:
            
            l1 = num[j] - num[j-1]
            l2 = num[j] - num[j-2]
            r1 = num[j] - num[j+1]
            r2 = num[j] - num[j+2]
            max_rex = [l1, l2, r1, r2]
            res.append(max(max_rex))
    print(sum(res))

# 한줄평 : 메모리 에러... 아마 리스트를 너무 많이 써서 에러가 난거같다.


# 2007번 패턴 마디의 길이

T = int(input())

for _ in range(1,T+1):
    txt = input() # 텍스트 입력
    res = 0 # 마디의 길이
    i = 1 # 패턴 분석용

    while True:
        if txt[0:i] == txt[i+1:2*i+1]: # 패턴의 반복 유무를 판단
            res = i + 1 # txt가 0부터 시작해서 1을 더해줌
            break # 패턴 분석이 끝나면 탈출
        
        i +=1 

    print(f"#{_} {res}") # 출력
