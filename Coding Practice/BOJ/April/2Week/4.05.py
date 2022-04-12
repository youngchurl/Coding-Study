# 1. Boj 2343번 기타레슨
'''n, m = map(int, input().split())
li = list(map(int, input().split()))

l = max(li)
r = sum(li)

while l<=r:
    mid = (l+r)//2
    tmd = []
    tem = 0

    for i in li:
        tem +=i
        if tem >=mid:
            tmd.append(tem)
            tem = 0
    if tem !=0:
        tmd.append(tem)

    if len(tmd)>m:
        l = mid+1
    else:
        r = mid -1


print(max(l,max(tmd)))
'''

# 두번째 풀이

'''n, m = map(int, input().split())
li = list(map(int, input().split()))

l = max(li)
r = sum(li)

while l<=r:
    mid = (l+r)//2
    cnt = 0
    tem = 0

    for i in range(len(li)):
        if tem+li[i] >mid:
            cnt +=1
            tem = 0
        tem += li[i]
    
    cnt +=1 if tem else 0

    if cnt>m:
        l = mid+1
    else:
        r = mid -1
print(l)'''

'''
리뷰 : 첫번째 코드도 내가 봤을때는 틀리지 않았기도하고 그리고 테스트 케이스도
통과했는데 왜 틀린지는 잘 모르겠다...
'''
