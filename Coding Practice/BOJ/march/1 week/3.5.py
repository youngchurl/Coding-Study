# 3.5
# 1. 백준 1789번 수들의 합
'''
1 : 1 / 1
2 : 1 / 2
3 : 2 / 1 2 
4 : 2 / 1 3
5 : 2 / 1 4
6 : 3 / 1 2 3 
7 : 3 / 1 2 4
8 : 3 / 1 2 5
9 : 3 / 1 2 6
10 : 4 / 1 2 3 4
수열의 형태를 띈다.
1, 3, 6, 10, 15
'''
import sys
input = sys.stdin.readline
num = int(input().rstrip())

cnt = 1 # 1,3,6 순으로 증가되는 수
d = 2 # 수열 증가폭
res = 1 # 각 숫자가 내포한 수 갯수
while cnt < num:
    res += 1
    cnt += d
    d += 1
if cnt == num :
    print(res)
else: 
    print(f'{res-1}')

'''
리뷰 : 처음에는 어떻게 풀어야될지 감도 안잡혀서 곤혹스러웠는데 수열임을 
 알고나면 어렵지 않은 문제였다.
'''
# 2. 백준 1946번 신입사원
# #첫번째 풀이 : 시간초과로 새롭게 풀어야합
import sys
input = sys.stdin.readline
tc = int(input().rstrip())
for _ in range(tc):
    num = int(input().rstrip())
    li = []
    res = [0 for _ in range(num)] # 평가자료
    for _ in range(num):
        li.append(list(map(int, input().split())))
    
    for i in range(num):
        for j in range(i,num):
            if i == j :
                pass
            else:
                if li[i][0] > li[j][0]:
                    res[i] += 1
                    pass
                if li[i][1] > li[j][1]: 
                    res[i] += 1
                
    print(res.count(0))
#두번째 풀이
import sys
input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    num = int(input().rstrip())
    li = [list(map(int, input().split())) for _ in range(num)]
    li.sort()
    mins = li[0][1]
    res = 1
    for i in range(1, num):
        if mins > li[i][1]:
            mins = li[i][1]
            res +=1
    print(res)

'''
리뷰 : 아직 효율적으로 짜는 방법을 몰라서 그런지 개인적으로는 어려운 문제였다...
첫번째 풀이가 생각나는대로 짠거였고 두번째는 좀 다듬고 이중 for문을 없애려고 노력한 결과인데
훨씬 간결해져서 반성이 됐고 앞으로도 이렇게 코드를 짤 수 있도록 노력해야겠다...
'''

# 3. 백준 1343번 폴리오미노

txt = input()
li = [] 
res = []
a = 'AAAA'
b = 'BB'
flag = True
tem = ''
cnt = 0
for i in txt:
    if i == 'X':
        cnt +=1
    elif i == '.':
        if cnt != 0:
            li.append(cnt)
        li.append(i)
        cnt = 0
if cnt != 0:
    li.append(cnt)

for j in li:
    if j =='.':
        res.append(j)
        pass
    elif (j%2) != 0:
        flag = False
        break

    else:
        while True:
            if j >=4:
                j -=4
                res.append(a)
                pass
            elif j >=2:
                j -=2
                res.append(b)
            if j ==0:
                break

if flag ==False:
    print('-1')
else:
    print("".join(res))

'''
리뷰 : 그리디 알고리즘이 점점 어려워지는게 체감이 되는 문제였다..
쉬운듯, 어려운듯 생각하기에 따라 다를거같다.
'''

# 4. 백준 16953번 A -> B x 아직 못품

a, b = map(int, input().split())
cnt = 1
check = True
check2 = True
if a*2 == b:
    check2 == False
while True:
    if (check == False) or (a==b):
        break
    if b < a :
        check = False

    if b % 2 == 0:
        b /=2
        cnt +=1

    elif b % 2 == 1:
        b //=10
        cnt +=1

if check2 == False:
    print('1')
    pass
elif check == True:
    print(cnt)
elif check == False:
    print('-1')
