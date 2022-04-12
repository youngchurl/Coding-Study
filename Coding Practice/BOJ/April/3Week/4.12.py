# 9237번 이장님 초대
n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
day = li[0]+1
cnt = 0
for i in li:
    cnt +=1
    day -=1
    if day<i:
        day = i
print(day + cnt)
'''
4 3 2 1 0
0 3 2 1 0
0 0 3 2 1 0
0 0 0 2 1 0
'''