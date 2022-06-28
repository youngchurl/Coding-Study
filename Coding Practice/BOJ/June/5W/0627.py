# 24416 알고리즘 수업
'''import sys
input = sys.stdin.readline
def fib(n):
    cnt1 = 0
    if n==1 or n==2:
        cnt1 +=1
        return cnt1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
# d = [0]*(n+1)
# d[1], d[2] = 1,1
# for i in range(3, n+1):
#     d[i] = d[i-1]+d[i-2]

print(fib(n),n-2)'''

# 9184 신나는 함수 실행

w = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
w[0][0][0] = 1
w[0][0][-1] = 1
w[0][-1][0] = 1
w[-1][0][0] = 1
w[0][-1][-1] = 1
w[-1][-1][0] = 1
w[-1][0][-1] = 1
w[-1][-1][-1] = 1
for k in range(21):
    for j in range(21):
        for i in range(21):
            if i==0 and j ==0 and k ==0:
                pass
            if i<j and j<k:
                w[i][j][k] = w[i][j][k-1]+w[i][j-1][k-1]-w[i][j-1][k]
            else:
                w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i][j-1][k]

while True:
    a,b,c = map(int, input().split())
    res = 0
    if a == -1 and b == -1 and c == -1:
        break
    elif a<=0 or b<=0 or c<=0:
        res = 1
    elif a>20 or b>20 or c>20:
        res = w[20][20][20]
    else:
        res = w[a][b][c]
    
    print(f'w({a}, {b}, {c}) = {res}')
