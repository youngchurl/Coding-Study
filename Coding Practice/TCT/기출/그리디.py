# 1 모험가 길드
n = int(input())
d = list(map(int, input().split()))
d.sort()
cnt = 0
print(d)
if len(d) == 1 and d[0] == 1:
    cnt +=1
else:
    for _ in range(n-1):      
        if len(d)< d[0]:
            break
        if d[0] ==1:
            d.pop(0)
            cnt +=1
        elif d[0] == 2:
            d.pop(0)
            d.pop()
            cnt +=1
        else:
            for j in range(d[0]-1):
                d.pop()
            d.pop(0)
            cnt+=1
    print(cnt)