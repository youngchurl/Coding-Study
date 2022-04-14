# 27 정렬된 배열에서 특정 수의 개수 구하기
def minin(li, x):
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