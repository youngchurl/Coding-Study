# 2.26

# SW 1859 백만 장자 프로젝트

tc = int(input())
for i in range(1, tc+1):
    n = int(input())
    li = list(map(int,input().split()))
    gain = 0

    li.reverse() # 가장 중요한 부분 리스트를 뒤집어서 이익을 계산!
    
    max_num = li[0] # 가장 큰 값으로 우선 넣어두고 큰 수가 나올때마다 바꾸는 방법으로 푼다.
    
    for j in range(n-1):
        if max_num >= li[j+1]:
            gain += (max_num - li[j+1])
        else:
            max_num = li[j+1]

    print(f'#{i} {gain}')
    
    
# 한줄평 : 예전에 못풀었던 백만장자문제... 풀이 방법을 알고 풀어서 그런지 그 당시보다 난이도가 쉬어짐을 느꼈다.

---

# SW 2005 파스칼의 삼각형

tc = int(input())

for n in range(1,tc+1):
    num = int(input())
    li = [[0]*num for _ in range(num)]
    li[0][0] = 1
    for i in range(1,num):
        for j in range(0,num):
            li[i][j] = li[i-1][j-1] + li[i-1][j]

    print(f'#{n}')
    for k in range(num):
        for res in li[k]:
            if res == 0:
                pass
            else:
                print(res,end=" ")
        print()
        
        
# 한줄평 : 스터디 처음엔 못풀었던 문제였는데 0으로 채우고 푸는법을 익히니깐 그래도 이젠 풀 수 있게됐다. 

---

# SW 2001 파리 퇴치

tc = int(input())

for i in range(1,tc+1):
    n,m = map(int, input().split())
    li = []
    res = 0 
    for _ in range(n):
        li.append(list(map(int, input().split()))) # 

    for j in range(n-m+1):
        for k in range(n-m+1):
            total = 0
            for l in range(m):
                total += sum(li[j+l][k:k+m])
                
            if res < total:
                res = total
        
    print(f'#{i} {res}')

# 한줄평 : 파리 퇴치라는게 너무 재밌는 주제였는데,  생각보다 어려웠고 3중 for문하면서 양심에 찔렸다....


# SW 1989 초심자의 회문 검사

tc = int(input())

for i in range(1, tc+1):
    txt = input()
    length = len(txt)//2
    cnt = 0
    l = 0
    r = -1
    flag = True
    while cnt != length:
        if txt[l] != txt[r]:
            flag = False
            break
        l +=1
        r -=1
        cnt+=1
    if flag == True:
        print(f'#{i} 1')
    else :
        print(f'#{i} 0')

# 한줄평 : 딱 보자마자 어떻게 짜야될지 감이 잡혔고 그대로 연산해서 바로 pass 할 수 있었다.

# SW 1986 지그재그 숫자

tc = int(input())

for i in range(1, tc+1):
    num = int(input())
    total = 0
    for j in range(1,num+1):
        if (j%2) != 0 :
            total +=j
        else:
            total -=j

    print(f'#{i} {total}')

# 한줄평 : 쉬운편에 속한단 생각이 들었던 문제, 별다른 아이디어 없이 풀린다.

# SW 1984 중간 평균값 구하기

tc = int(input())

for i in range(1,tc+1):
    num_li = list(map(int,input().split()))
    num_li.sort()
    num_li.pop(0)
    num_li.pop(-1)
    mean = round(sum(num_li)/len(num_li))
    print(f'#{i} {mean}')

# 한줄평 : 쉽게 풀 수 있었던 문제!

# 1983 조교의 성적 매기기

tc = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1,tc+1):
    n,k = map(int, input().split())
    check = n/10

    dic = {}
    for j in range(1, n+1):
        a, b, c = map(int, input().split())
        total = round(((a * 0.35) + (b * 0.45) + (c * 0.2)))
        dic.setdefault(j,total)
        
    dic_sort = sorted(dic.values(), reverse=True)
    rank = dic_sort.index(dic[k])
    rank2 = round(rank//check)

    print(f'#{i} {score[rank2]}')

# 한줄평 : 딕셔너리 정렬에 대해서 다시한번 고민해보고 실습 할 수 있는 문제였다. 마지막 딕셔너리 정렬부분만 거의 15분은 고민한거같은데 좀 더 연습해야될 필요성을 느낀다....


# SW 1976 시각 덧셈

tc = int(input())

for i in range(1,tc+1):
    li = list(map(int, input().split()))
    hour = li[0] + li[2]
    minute = li[1] + li[3]

    if minute >= 60:
        minute -=60
        hour +=1
    if hour >=13:
        hour -=12
    print(f'#{i} {hour} {minute}')

# 시간 문제는 백준에서도 한번 풀어봐서 그런지 쉽게 풀 수 있었다.
