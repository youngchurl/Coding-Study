# 라디오
tmd,goal = map(int, input().split())
n = int(input())
res = abs(goal-tmd)
flag = True
cnt = 0
for _ in range(n):
    tem = int(input())
    tem2 = abs(goal-tem)
    if res > tem2:
        flag = False
        res = tem2
if flag == False:
    cnt +=1
print(cnt+res)