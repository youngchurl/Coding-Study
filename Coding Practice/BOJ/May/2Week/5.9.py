# 15501 부당한 퍼즐
from collections import deque
n = int(input())
li1 = deque(list(map(int, input().split())))
li2 = deque(list(map(int, input().split())))

mid = n//2

while li1[mid] !=mid+1:
    li1.appendleft(li1.pop())
while li2[mid] !=mid+1:
    li2.appendleft(li2.pop())
li3 = sorted(li2)

if list(li1)==list(li2) or list(li1) ==li3:
    print('good puzzle')
else:
    print('bad puzzle')