# 2022.02.11

# SW 1954 달팽이 숫자

for n in range(1, int(input())+1):

    num = int(input())

    row = 0
    col = 0

    mat = [[0 for _ in range(num)] for _ in range(num)]

    l, r, u, d = 0, num-1, 1, num-1 # 경계
    row_change = True # 행 이동 
    col_change = True # 열 이동
    for i in range(1,num**2 + 1):

        if row_change == True and col_change == True:
            mat[row][col] = i
            col +=1

            if col == r :
                mat[row][col] = i
                row_change = False
                r -=1
                

        elif row_change == False and col_change == True:
            mat[row][col] = i
            row +=1

            if row == d :
                mat[row][col] = i
                col_change = False
                d -=1
                

        elif row_change == False and col_change == False:
            mat[row][col] = i
            col -=1

            if col == l :
                mat[row][col] = i
                row_change = True
                l +=1

        elif row_change == True and col_change == False:
            mat[row][col] = i
            row -=1

            if row == u :
                mat[row][col] = i
                col_change = True
                u +=1

    print(f"#{n}")
    for _ in mat:
        print(*_)
        
한줄평 : 푸는데 걸린시간 약 2~3시간.... 구상은 쉽게 했는데 구현이 어려웠던 문제... 


2005 파스칼의 삼각형

T = int(input())

for i in range(1,T+1):
    num = int(input())
    
    if num == 1:
        print(f"#{i}")
        print("1")
    else:
        print(f"#{i}")
        for j in range(num):
            for k in range()

2022.02.15

SW 1979. 어디에 단어가 들어갈 수 있을까?

tc = int(input())

for i in range(1, tc+1):
    n,k = map(int, input().split())
    mat = []
    for j in range(n):
        mat.append(list(input().split()))
    res = 0

    for a in range(n):
        cnt = 0
        for b in range(n):
            if mat[a][b] == '1':
                cnt +=1
            
            if mat[a][b] == '0' or b == n-1:
                if cnt == k:
                    res +=1
                cnt = 0
        for c in range(n):
            if mat[c][a] == '1':
                cnt +=1

            if mat[c][a] == '0' or c == n-1:
                if cnt == k:
                    res +=1
                cnt = 0
    print(f'#{i} {res}')

13218 조별과제

for i in range(1, int(input())+1):
    num = int(input())
    print(f'#{i} {num//3}')

백준 11279번 최대힙

import sys
import heapq

heap = []
tc = sys.stdin.readline()
for i in range(int(tc)):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(-1 * heapq.heappop(heap))
    elif n > 0 :
        heapq.heappush(heap, (-n))
