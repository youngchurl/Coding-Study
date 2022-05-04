'''
1 : 1
2 : 1 + 1, 2
3 : 1+1+1, 1+2, 2+1, 3
'''
'''from itertools import permutations
import sys
input = sys.stdin.readline
n,k = map(int, input().split())

d=[[] for _ in range(11)]
d[1] = ['1']
d[2] = ['1+1','2','2']
d[3] = ['1+1+1', '1+2', '2+1', '3']
for i in range(4,n+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]
tmd = list(permutations(d[n], 2))
tmd2 = []
for i in tmd:
    a, b = i[0], i[1]
    if eval(a) + eval(b) == n:
        tmd2.append(i)
res = []
for i in tmd2:
    a,b = i[0],i[1]
    res.append(a+'+'+b)
res = list(set(res))
res.sort()

if k > len(res):
    print('-1')
else:
    print(res[k-1])'''


# 두번째


'''from itertools import permutations
import sys

input = sys.stdin.readline
n,k = map(int, input().split())

d=[[] for _ in range(11)]

if n>=4:
    d[1] = ['1']
    d[2] = ['1+1','2','2']
    d[3] = ['1+1+1', '1+2', '2+1', '3']
    for i in range(4,n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]
    tmd = list(permutations(d[n], 2))

    res = []
    for i in tmd:
        a,b = i[0],i[1]
        c = a+'+'+b
        if eval(c)==n:
            res.append(c)
    res = list(set(res))
    res.sort()

    for i in range(4,n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]
    tmd = list(permutations(d[n], 2))
    tmd2 = []
    for i in tmd:
        a, b = i[0], i[1]
        if eval(a) + eval(b) == n:
            tmd2.append(i)
    res = []
    for i in tmd2:
        a,b = i[0],i[1]
        res.append(a+'+'+b)
    res = list(set(res))
    res.sort()


    print(res)
    if k > len(res):
        print('-1')
    else:
        print(res[k-1])
else:
    d[1] = ['1']
    d[2] = ['1+1','2']
    d[3] = ['1+1+1', '1+2', '2+1', '3']
    if k> len(d[n]):
        print('-1')
        
    else:
        print(d[n][k-1])'''


