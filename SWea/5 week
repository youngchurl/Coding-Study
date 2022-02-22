# 2022.02.17

# SW 1928. Base64 Decoder / D2

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

dic = {}

for i,j in enumerate(a): # 딕셔너리에 Base64 입력
    dic[j] = i

tc = int(input())

for i in range(1, tc+1):
    txt = input()
    li = []
    num = ""
    for j in txt:
        n2 = bin(dic[j])[2:].zfill(6) # 2진법으로 변환 0b는 제거, zfill을 통해 6칸짜리로
        num +=n2 # 2진법을 그냥 일렬로 쭉 나열

    res =""
    while num:
        res = int('0b'+num[:8], 2) # 2진법을 숫자로 변환(아스키 코드) 
        li.append(chr(res)) # 아스키코드를 문자로 변환 및 list에 담아둠
        num = num[8:] # 사용한 2진법은 제거
    print(f'#{i} '+"".join(li))
    
# 한줄평 : 이진법변환, 아스키코드변환, zfill등 기초공부할때 했었던걸 복습한 느낌이었다..


1208번 Flatten
import sys
input = sys.stdin.readline

for i in range(1,11):
    num = int(input())
    li = list(map(int, input().split()))
    li2 = sorted(li)
    while num != 0 :
        li2[0] += 1
        li2[99] -= 1
        li2.sort()
        num -= 1
    res = max(li2)-min(li2)
    print(f'#{i} {res}')

한줄평 : 직관적으로 풀었는데 바로 풀려서 솔직히 당황했다.... 

2805번 농작물 수확하기

tc = int(input())

for i in range(1,tc+1):
    n = int(input())
    non = (n-1)//2
    di = True
    cnt = 0
    sum_res = 0

    for j in range(n):    
        cul = input()
        
        if non - cnt == 0: 
            di = False

        if cnt == 0:
            res = cul[non]
        elif cnt !=0:
            res = cul[non-cnt:non+cnt+1]
        if di == True:
            cnt +=1
        elif di == False:
            cnt -=1

        for k in res:
            sum_res += int(k)

    print(f'#{i} {sum_res}')

한줄평 : 그렇게 어렵다 하는 싶은건 없었고 직관적으로 풀었다.

2022.02.21

1974번 스도쿠 검증
총합 : 45 
tc = int(input())
for i in range(1, tc+1):
    mark = True
    row = []
    col = [0 for _ in range(9)]
    sq1,sq2,sq3 = 0, 0, 0    

    for j in range(9):

        row = list(map(int, input().split()))

        if sum(row) !=45: # row 체크
            mark = False
            break

        # 각 col에 값 입력
        for k in range(9):
            col[k] += row[k]
         
        # 각 3x3 공간 체크
        sq1 = sum(row[0:2])
        sq2 = sum(row[3:5])
        sq3 = sum(row[6:8])
        if j == 2 or j == 5:
            if sq1 != 45 or sq2 != 45 or sq3 !=45:
                mark = False
            sq1,sq2,sq3 = 0,0,0

        row = []

    for m in range(9):
        if col[m] != 45:
            mark = False

    if mark == False:
        print(f"#{i} 0")
    else:
        print(f"#{i} 1")

한줄평 : 합이 45가 안되면 에러로 뽑았는데 예상은 했지만 역시나 안됐다..

tc = int(input())
sq1, sq2,sq3 = [],[],[]

for i in range(1,tc+1):
    for j in range(9):
        row = list(map(int, input().split()))
        
        mat = []
        mat.append(row)
        mark = True

        # 3x3 구역별 저장
        sq1.append(row[0:2])
        sq2.append(row[3:5])
        sq3.append(row[6:8])

        for k in range(1, 10):
            if row.count(j) != 1 or sq1.count(j) != 1 or sq2.count(j) != 1 or sq3.count(j) != 1:
                mark = False 

        if j ==2 or j ==5:
            sq1.clear
            sq2.clear
            sq3.clear
        row.clear

    col = [0 for _ in range(9)]

    for j in range(9):
        for k in range(9):
            if col[j] == mat[k][j]:
                col[j] +=1

    for j in range(9):
        if col[j] != 9:
            mark = False
    
    if mark == False:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')

한줄평 : 이번엔 각 1~9까지 숫자가 하나보다 많냐?로 기준을 정했는데 런타임 오류가 나왔다..
