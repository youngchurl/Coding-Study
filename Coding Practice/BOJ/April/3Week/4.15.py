# 2417번 정수 제곱급
'''n = int(input())
l = 0
r = 2**63
flag = False
while l<=r:
    mid = (l+r)//2
    if mid >=n:
        r = mid-1
    else:
        if mid**2 == n:
            flag = True
            break
        if mid**2<n:
            l = mid+1
        else:
            r = mid-1
if flag == True: print(mid)
print(r)
'''
'''
n = int(input())
l = 0
r = 2**63

while l<=r:
    mid = (l+r)//2
    res = mid**2
    if res<n:
        l = mid+1
    else:
        r = mid-1
print(l)
    '''

# 2776번 암기왕
tc = int(input())
for _ in range(tc):
    n = int(input())
    li = list(map(int, input().split()))
    dic = {i:1 for i in li}
    m = int(input())
    li2 = list(map(int, input().split()))

    for i in li2:
        if i in dic.keys():
            print(1)
        else:
            print(0)