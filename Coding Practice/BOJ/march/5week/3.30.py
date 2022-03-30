# 1. 6236번 용돈관리
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

money = [int(input()) for _ in range(n)]

l = 1
r = sum(money)

while l<=r:
    mid = (l+r)//2
    cnt = 0
    tem = 0
    flag = False
    for i in money:
        if tem <i:
            if mid >=i:
                tem = 0
                tem +=mid
                tem -=i
                cnt +=1
            else:
                flag = True
        else:
            tem -=i

    if cnt>m or flag==True:
        l = mid+1
    else:
        r = mid-1
print(l)