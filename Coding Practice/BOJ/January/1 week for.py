2022.01.22

# 백준 2739번 구구단

N = int(input()) # N으로 입력값 받기
for _ in range(1,9+1): print(f"{N} * {_} = {N*_}")

# 백준 10950번 A+B -3
T = int(input()) # 테스트 케이스의 개수
for _ in range(T): 
    a,b = map(int, input().split()) # 각 케이스의 A,B값 입력
    print(f'{a+b}') # A+B 출력
    
# 8393번 합
n = int(input()) # 숫자 n 값 입력
total = 0 # 총합

for i in range(1,n+1): total += i # total에 1 ~ n을 더함

print(f'{total}') # 총합을 출력

# 15552번 빠른 A+B
import sys

T = int(sys.stdin.readline()) # 테스트 케이스도 stdin으로 받음

for _ in range(T):
    a,b = map(int, sys.stdin.readline().split()) 
    print(f'{a+b}')

# 2741번 N 찍기
n = int(input())
for _ in range(1,n+1): print(f'{_}')

# 2742번 기찍 N
import sys
n = int(sys.stdin.readline())
for _ in range(n,0,-1): print(_)

# 11021번 A+B - 7
T = int(input())

for _ in range(1,T+1):
    a,b = map(int, input().split())
    print(f'Case #{_}: {a+b}')
    
#  11022번 A+B - 8

T = int(input()) # 테스트 케이스 입력

for i in range(1,T+1): # 테스트 케이스 번호 1 부터 시작
    a, b = map(int, input().split()) # a,b 값을 입력
    print(f'Case #{i}: {a} + {b} = {a+b}') 

# 2438번 별찍기 - 1 

# for i in range(1,int(input())+1): print('*'*i)    

# 2439번 별찍기 - 2

n = int(input()) # 별 층 입력

for i in range(1,n+1): 
    print("{}{}".format(' '*(n-i),'*'*i)) # 공백과 별을 따로 포맷으로 기입


# 10871번 X 보다 작은 수

n, x = map(int, input().split()) # 수열 A의 갯수 n 과 정수 x 입력 
arr = list(map(int, input().split())) # 숫자를 리스트로 받는다.
res = [] # 빈 리스트 

for i in arr: 
    if i < x: res.append(i) # x보다 작을 때 res 에 담는다.

for _ in res: print(f'{_}', end=' ') # 리스트에서 차례대로 꺼내서 출력
  



