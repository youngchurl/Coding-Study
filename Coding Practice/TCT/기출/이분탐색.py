# 27 정렬된 배열에서 특정 수의 개수 구하기
'''def minin(li, x):
    l = 0
    r = len(li)
    x = x-1
    while l<=r:
        mid = (l+r)//2
        if len(li)<=mid:
            r = mid-1
            pass
        else:
            res = li[mid]

            if res>x:
                r = mid-1
            else:
                l = mid +1
    return l

def maxin(li, x):
    l = 0
    r = len(li)
    x = x+1
    while l<=r:
        mid = (l+r)//2
        if len(li)<=mid:
            r = mid-1
            pass
        else:
            res = li[mid]

            if res>x:
                r = mid-1
            else:
                l = mid +1
    return l


n, x = map(int, input().split())
li = list(map(int, input().split()))
if li[-1] < x:
    print('-1')
else:
    a = minin(li,x)
    b = maxin(li,x)
    print(b-a-1)
'''

# 28 고정점 찾기
n = int(input())
li = list(map(int ,input().split()))

le = len(li)
l = 0
r = le-1
flag = False

while l<=r:
    mid = (l+r)//2
    if mid > le:
        r = mid-1

    else:
        if li[mid] == mid:
            l = mid
            flag = True
            break
        if li[mid]>mid:
            r = mid-1
        else:
            l = mid+1
if flag == True:
    print(l)
else:
    if li[l] == l:
        print(l)
    else:
        print('-1')