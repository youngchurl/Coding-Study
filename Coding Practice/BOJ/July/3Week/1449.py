# 1449번 수리공 항승
n , l =map(int, input().split())
li = list(map(int, input().split()))
li.sort()
tmd = li[0]
cnt = 1
for i in range(len(li)):
    if li[i]>=tmd+l:
        tmd = li[i]
        cnt +=1
print(cnt)