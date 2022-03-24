# 1. Boj 13706번 제곱근
# n = int(input())
# l = 1
# r = n

# while l<=r:
#     mid = (l+r)//2

#     if mid**2 == n:
#         print(mid)
#         exit()
#     if mid**2 < n:
#         l=mid+1
#     else:
#         r = mid-1
# print(l)

# 2. Boj 17266번 어두운 굴다리
# n = int(input())
# m = int(input())

# lamp= list(map(int, input().split()))

# res = [lamp[0], n-lamp[-1]]

# for i in range(1,m):
#     tem = lamp[i]-lamp[i-1]
#     if tem%2==0:
#         tem //=2
#     else:
#         tem =(tem//2)+1
#     res.append(tem)

# print(max(res))

'''
리뷰: 거의 다풀었다 싶은 경우였는데 왜이리 안풀리지? 하고 고민했는데
귀찮아서 설마 하고 라운드 썼던거때매 자꾸 틀렸던거였다...
'''

# 3. 7795번 먹을 것인가 먹힐 것인가

# tc = int(input())
# for _ in range(tc):
#     n, m =map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     a.sort()
#     b.sort()
#     res = []
#     for i in b:
#         l = 0
#         r = len(a)-1
        
#         while l <= r:
#             mid =(l+r)//2
#             if a[mid]>i:
#                 r=mid-1
#             else:
#                 l=mid+1
#         res.append(len(a)-l)
#     print(sum(res))

'''
리뷰 : 난이도와 별개로 이걸 어떻게 이분탐색으로 풀지? 를 고민했다. 인덱스로
대소 비교도 가능하다는점을 알았다!
'''

# 4. 16401번 과자 나눠주기
# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# li = list(map(int, input().split()))
# l = 1
# r = max(li)

# while l<=r:
#     mid=(l+r)//2
#     cnt = 0
#     for i in li:
#         if i-mid>=0:
#             cnt += i//mid

#     if cnt>=n:
#         l = mid+1
#     else:
#         r = mid-1
    
# print(r)
'''
리뷰 : 쉬운듯 어려운듯한 문제..
'''

# 5. 1012번 유기농 배추
'''from sys import stdin, setrecursionlimit
setrecursionlimit(2000)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bug(x,y):
    global dx
    global dy
    global x1
    global y1
    global flag
    if mat[x][y] == 0:
        return 0         
    else:
        flag = True
        mat[x][y] = 0
        for i in range(4):
            x1 =x+dx[i]
            y1 =y+dy[i]

            if 0<=x1<m and 0<=y1<m:
                if mat[x1][y1] ==1:
                    flag = True
                    return bug(x1,y1)
                else:
                    flag = False
        if flag ==False:
            return 1

tc = int(stdin.readline())
for _ in range(tc):
    m, n, k = map(int, stdin.readline().rstrip().split())
    mat = [[0]*(n+1) for _ in range((m+1))]
    for _ in range(k):
        a,b = map(int, stdin.readline().rstrip().split())
        mat[a][b] = 1
    res = []
    for i in range(m):
        for j in range(n):
            res.append(bug(i,j))
    print(sum(res))'''

    '''
    아직 못품
    '''

    # 5. 마인크래프트
n ,m ,k = map(int, input().split())
li = []
for i in range(n):
    tem = list(map(int, input().split()))
    for j in tem:
        li.append(j)

