# 1. 백준 2920번 음계
li = list(map(int, input().split()))
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]
if li == ascending:
    print("ascending")
elif li == descending:
    print("descending")
else:
    print('mixed')

'''
리뷰 : 음... 다른 어려운 문제 풀다가 백준 등급 올리고 싶어서 필수 문제를
풀어본건데 솔직히 난이도가 굉장히 쉬웠다. 이렇게 푸는건지는 모르겠다..
'''

# 2. 2475번 검증수

li = list(map(int, input().split()))
res = 0
for i in li:
    res += i**2
print(res%10)
'''
리뷰 : 하나씩 꺼내서 제곱수를 더할 수만있다면 쉽게 풀 수 있는 문제
'''

# 3. 11050번 이항계수
import sys
sys.setrecursionlimit(10**6)

def fac(n):
    if n == 1 or n == 0 :
        return 1
    return n*fac(n-1)

n, k = map(int, input().split())

n_k = n-k
print(round(fac(n)/(fac(k)*fac(n_k))))

'''
리뷰: 별다른 어려운 점은 없었고 백준에서 setrecursionlimit를 이용해
재귀의 한계를 조정할 수 있음을 알았다.
물론 이 문제는 재귀 한계 조정 없이 풀 수 있다.
'''

# 4. 10845번 큐
import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())
deq = deque()

for _ in range(tc):
    order = input().split()
    if order[0] == 'push':
        deq.append(order[1])
    if order[0] == 'pop':
        if deq:
            print(deq[0])
            deq.popleft()
        else:
            print('-1')
    if order[0] == 'size':
        print(len(deq))
    if order[0] == 'empty':
        if deq:
            print('0')
        else:
            print('1')
    if order[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print('-1')
    if order[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print('-1')

'''
리뷰: 큐에 대해서는 대강 알고 있었고 덱을 이용해서 푸니깐 아주 쉬운 문제였다.
'''
