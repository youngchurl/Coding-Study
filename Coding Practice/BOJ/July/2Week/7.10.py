# 2477 참외밭
'''
동쪽 : 1
서쪽 : 2
남쪽 : 3
북쪽 : 4
'''
n = int(input())
li = []
dir = [0,0,0,0] # 동 서 남 북
ch = [0,0,0,0,0,0]
cnt = 1
for j in range(6):
    a,b = map(int, input().split())
    li.append([a,b])
    dir[a-1] +=1

for i in range(6):
    if dir[li[i][0]-1] == 1:
        ch[i] +=cnt
        cnt +=1
big_rec = li[ch.index(1)][1]*li[ch.index(2)][1]
small_rec = li[(ch.index(2)+2)%6][1]*li[(ch.index(2)+3)%6][1]

res = big_rec - small_rec
print(res*n)