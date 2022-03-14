# 
# 1이 될때 까지

'''
1. n -1 
2. n/k
'''
# m,k = map(int, input().split())
# cnt = 0
# while m !=1:
#     if m %k==0:
#         m /=k
#         cnt +=1
#     else:
#         m -=1
#         cnt +=1
# print(cnt)

# 더하거나 곱하거나

# txt = input()
# li = [int(i) for i in txt]
# res = li[0]
# for i in range(len(txt)-1):
#     if li[i]<=1 or li[i+1]<=1:
#         res +=li[i+1]
#     else:
#         res *=li[i+1]
# print(res)

# 모험가 길드

# n = int(input())
# li = list(map(int, input().split()))
# li.sort()
# people = len(li)
# res = 0
# num = 0
# while True:
#     if people >= li[num]:
#         people -=li[num]
#         num +=li[num]
#         if num >=n:
#             break
#         res +=1
#     else:
#         break
# print(res)

# 상하 좌우 문제

# dx = [1,0,-1,0] # 우측, 좌측
# dy = [0,1,0,-1] # 아래, 위
# n = int(input())
# li =[[0]*n for _ in range(n)] # 맵
# x = 1
# y = 1

# order = list(map(str, input().split()))

# for i in order:
#     if i=='R' and x<n:
#         x +=dx[0]
#     elif i == 'L'and x>1:
#         x += dx[2]
#     elif i=='U'and y>1:
#         y +=dy[3]
#     elif i == 'D'and y<n:
#         y += dy[1]
# print(x,y)

# 시각 3이 포함되면 카운트!

# n = int(input())
# cnt = 0
# hour = 0
# minute = 0
# sec = 0
# while hour <= n:
#     sec +=1
#     if sec ==60:
#         minute +=1
#         sec -=60
#     if minute == 60:
#         hour +=1
#         minute -=60
#     check = str(sec) + str(minute) + str(hour)
#     if check.count('3') >=1:
#         cnt +=1
# print(cnt)

# 왕실의 나이트

# dx = [-1, 0, 1, 0] # 좌, 우
# dy = [0, -1, 0, 1] # 위, 아래

# mat = [[0]*8 for _ in range(8)]
# al = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h']
# num = ['1', '2', '3', '4', '5', '6', '7', '8']

# order = input()
# res = 0

# x = al.index(order[0])
# y = num.index(order[1])

# if (x-2) >=0:
#     if (y-1) >=0:
#         res +=1
#     elif (y+1) >=0:
#         res +=1
#     else:
#         pass
#     pass

# if (x+2) <=7:
#     if (y-1) >=0:
#         res +=1
#     elif (y+1) >=0:
#         res +=1
#     else:
#         pass
#     pass

# if (y-2) >=0:
#     if (x-1) >=0:
#         res +=1
#     elif (x+1) >=0:
#         res +=1
#     else:
#         pass
#     pass

# if (y+2) <=7:
#     if (x-1) >=0:
#         res +=1
#     elif (x+1) >=0:
#         res +=1
#     else:
#         pass
#     pass

# print(res)

# 문자열 재정렬
# n = '0123456789'
# txt = input()
# li = []
# num = 0
# for i in txt:
#     if not i in n:
#         li.append(i)
#     else:
#         num += int(i)
# li.sort()

# print("".join(li)+str(num))


# 이코테 4장 실전문제 게임개발

n,m = map(int,input().split())
x,y,d = map(int,input().split())
# 초기 방향 설정시 사용
dic = {0:0, 1:3, 2:2, 3:1}
s = dic[d]
# 나아갈 방향 북,서,남,동
di = [(0,-1), (-1,0),(0,1),(1,0)] 
mat =[list(map(int, input().split())) for _ in range(n)] # 맵 만들기

mat[x][y] = 1 # 한번 지나간 곳은 바다로 만든다.
lo =[x,y] # 케릭터 위치
res = 1 # 밟고 있는땅 포함
cnt = 1 

while True:
    lo[0] +=di[s][0]
    lo[1] +=di[s][1]
    if mat[lo[0]][lo[1]] ==1:
        # 방향이 옳지 않기때문에 다시 뒤로 돌아간다.
        lo[0] -=di[s][0]
        lo[1] -=di[s][1]

        cnt +=1# 방향 전환할때마다 1씩증가
        s +=1 # 방향을 바꿈
        s %=4 

        if cnt ==4:
            break
    else:
        mat[lo[0]][lo[1]] =1 # 땅을 밟았기 때문에 초기화
        cnt = 0 # 방향 cnt도 초기화
        res +=1
print(res)

'''
리뷰: 난이도가 막 어렵진 않았는데, 중간에 실수를 해서 문제가 제대로 안풀렸다..
'''

