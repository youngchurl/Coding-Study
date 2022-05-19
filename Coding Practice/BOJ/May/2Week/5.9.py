# 15501 부당한 퍼즐
from collections import deque
n = int(input())
li1 = deque(list(map(int, input().split())))
li2 = deque(list(map(int, input().split())))

mid = n//2

while li1[mid] !=mid+1:
    li1.appendleft(li1.pop()) # 1 2 3 4 5
while li2[mid] !=mid+1:
    li2.appendleft(li2.pop()) # 2 3 4 5 1
li3 = sorted(li2)

if list(li1) == list(li2) or list(li1) == li3:
    print('good puzzle')
else:
    print('bad puzzle')


# 9465번 스티커

# for _ in range(int(input())):
#     n = int(input())
#     l1 = list(map(int, input().split()))
#     l2 = list(map(int, input().split()))
#     l1.append(0)
#     l2.append(0)

#     d = [0]*(n+2)
#     res = 0
#     for i in range(n+1):
#         a = l1[i-1]+l2[i+1]
#         b = l2[i-1]+l2[i+1]
#         c = l1[i-1] + l2[i] + l1[i+1]
#         d = l2[i-1] + l1[i] + l2[i+1]
#         if a>max(c,d) or b>max(c,d):
#             pass
#         else:
            


t = int(input())
for i in range(t):
    s = []
    n = int(input())
    
    for k in range(2):
        s.append(list(map(int, input().split())))
    
    for j in range(1, n):
        if j == 1:
            s[0][j] += s[1][j - 1]
            s[1][j] += s[0][j - 1]
        else:
            s[0][j] += max(s[1][j - 1], s[1][j - 2])
            s[1][j] += max(s[0][j - 1], s[0][j - 2])
        
    print(max(s[0][n - 1], s[1][n - 1]))

