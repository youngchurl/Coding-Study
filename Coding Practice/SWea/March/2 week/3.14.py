# 1번. SW 1284 수도요금 경쟁
# tc = int(input())
# # p: 리터당 요금, q : r리터 이하 요금, r: 기본요금제한, s 리터당 요금, w 사용량

# for i in range(1,tc+1):
#     p,q,r,s,w = map(int,input().split())
#     a = w*p
#     if r >=w:
#         b = q
#     else:
#         b = (w-r)*s + q
    
#     if a<=b:
#         print(f'#{i} {a}')
#     else:
#         print(f'#{i} {b}')

# 2번 SW 1288 새로운 불면증 치료법
# tc = int(input())
# for i in range(1,tc+1):
#     num = int(input())
#     dic = {str(j):0 for j in range(10)}
#     cnt = 0
#     n = num

#     while 0 in dic.values():
#         txt_n = str(n)
#         for k in txt_n:
#             dic[k] += 1
#         cnt +=1
#         n +=num
#     res = num*cnt
#     print(f'#{i} {res}')

'''
리뷰 : 딕셔너리가 익숙하지 않아서 좀 써보려다가 오래 걸린 문제...
난이도 자체가 어렵진않았다.
'''
# 3번 SW 1940 가랏! RC카!

# tc = int(input())

# for i in range(1,tc + 1):
#     res = 0
#     acc = 0
#     for _ in range(int(input())):
#         li = list(map(int, input().split()))
#         if len(li) == 2 :
#             o, a=li[0],li[1]
#         else:
#             o = li[0]

#         if o == 2:
#             acc -=a
#             if acc <0:
#                 acc = 0
#         elif o == 1:
#             acc +=a
#         res +=acc
#     print(f'#{i} {res}')

'''
리뷰 : 처음 문제 시작할때 우려했던대로 명령이 하나일때 두개일때를 
구분 지어야 한단 점을 제외하면 어려울건 없던 문제였다.
'''

# 4번 SW 1945번 간단한 소인수분해
# tc = int(input())
# for i in range(1,tc+1):
#     n = int(input())
#     li = [2,3,5,7,11]
#     res = [0 for _ in range(5)]
    

#     for j in li:
#         while n%j == 0:
#             n //=j
#             res[li.index(j)] +=1

#     print(f'#{i}',*res)

'''
리뷰 : 어려움없이 풀 수 있는 문제다.
'''
# 5번 1946번 간단한 압축 풀기
# tc = int(input())
# for i in range(1,tc+1):
#     print(f"#{i}")
#     li = []
#     for _ in range(int(input())):
#         txt, n = map(str, input().split())
#         for j in range(int(n)):
#             li.append(txt)
#     for k in range(len(li)):
#         print(li[k],end='')
#         if k%10 == 9:
#             print()
#     print()

'''
리뷰 : 답이 맞는데 안풀리는 점이 있어서 고민했는데 개행문자 하나 차이였다...
'''

# 6. SW 1948 날짜 계산기
# mon = [0,31, 28, 31, 30,31,30,31,31,30,31,30,31]
# tc = int(input())
# for i in range(1, tc+1):
#     sm, sd, em, ed = map(int, input().split())
#     res = 0
#     if sm == em:
#         res = ed - sd +1
#     else:
#         res +=sum(mon[sm:em])
#         res +=(ed - sd)+1
#     print(f'#{i} {res}')

'''
리뷰 : 직관적으로 풀면 어렵지 않다.
'''

# 7. SW 1959번 두개의 숫자열
# tc = int(input())
# for i in range(1,tc+1):
#     a,b = map(int,input().split())
#     li1 = list(map(int, input().split()))
#     li2 = list(map(int, input().split()))
#     res = []

#     if a==b:
#         for j in range(a):
#             res +=li1[j]*li2[j]

#     elif a>b:
#         tem = 0
#         for j in range(a-b+1):
#             for k in range(b):
#                 tem +=li1[j+k]*li2[k]
#             res.append(tem)
#             tem = 0
    
#     else:
#         tem = 0
#         for j in range(b-a+1):
#             for k in range(a):
#                 tem +=li1[k]*li2[j+k]
#             res.append(tem)
#             tem = 0
#     res.sort(reverse=True)
#     print(f'#{i} {res[0]}')

'''
리뷰: 구현자체가 어렵진않았는데 이보다 효율적인 코드로 짜야한다면
머리좀 아플꺼같다...
'''
# 8. SW 1961번 숫자 배열 회전

# def an90(n,mat):
#     new_mat = []
#     for i in range(n):
#         for j in range(n-1,-1,-1):
#             new_mat.append(mat[j][i])
#     return new_mat

# def an180(n,mat):
#     new_mat = []
#     for i in range(n-1,-1,-1):
#         for j in range(n-1,-1,-1):
#             new_mat.append(mat[i][j])
#     return new_mat

# def an270(n,mat):
#     new_mat = []
#     for i in range(n-1,-1,-1):
#         for j in range(n):
#             new_mat.append(mat[j][i])
#     return new_mat

# tc = int(input())
# for t in range(1,tc+1):
#     n = int(input())
#     mat = []
#     for _ in range(n):
#         mat.append(list(map(int,input().split())))
    
#     a90 = an90(n,mat)
#     a180 = an180(n,mat)
#     a270 = an270(n,mat)
#     print(f'#{t}')
#     for i in range(n):
#         a = a90[n*i:n*(i+1)]
#         b = a180[n*i:n*(i+1)]
#         c = a270[n*i:n*(i+1)]
#         for j in a:
#             print(j,end='')
#         print(' ',end='')
#         for j in b:
#             print(j,end='')
#         print(' ',end='')
#         for j in c:
#             print(j,end='')
#         print()

'''
리뷰 : 함수를 본격적으로 써본것도 처음이고, range에서 reversed(range(n))으로
사용이 가능하다는걸 처음으로 알 수 있어서 배울점이 많은 문제였다. 
'''

# 8. SW 1974번 스도쿠 검증
# tc = int(input())
# for t in range(1,tc+1):
#     check = [i for i in range(1,10)] # 정답지
#     check = set(check)
#     res = 1
#     mat = []
#     # 스도쿠 제작
#     for _ in range(9):
#         mat.append(list(map(int, input().split())))

#     for p in range(9):
#         if set(mat[p]) != check:
#             res = 0
#             break

#     if res == 1:
#         col_mat = list(map(list, zip(*mat)))
#         for q in range(9):
#             if set(col_mat[q]) != check:
#                 res = 0
#                 break

#         for i in range(3):
#             for l in range(3):
#                 tem = []
#                 for j in range(3):
#                     for k in range(3):
#                         tem.append(mat[3*i+j][3*l+k])

#                 if set(tem) != check:
#                     res = 0
#                     break
#     print(f'#{t} {res}')

'''
리뷰: 스터디할때 풀어봤던 문제임에도 이번에 푸는데 엄청 어렵게 느껴졌다...
푸는 방법은 대강 아는데도 구현이 안되니깐
문법적인 지식을 좀 더 알아둘 필요성을 느꼈다.
추가적으로 zip과 언패킹을 통해서 행렬의 col, row 변환하는법을 익힐 수 있는
문제다.
'''
# 이코테 4장 실전문제 게임개발

n,m = map(int,input().split())
x,y,d = map(int,input().split())
dic = {0:0, 1:3, 2:2, 3:1} # 초기 방향 설정시 사용
s = dic[d]
di = [(0,-1), (-1,0),(0,1),(1,0)] # 나아갈 방향 북,서,남,동
mat =[list(map(int, input().split())) for _ in range(n)]

mat[x][y] = 1 # 한번 지나간 곳은 바다로 만든다.
lo =[x,y]
res = 1
cnt = 1
while True:
    lo[0] +=di[s][0]
    lo[1] +=di[s][1]
    if mat[lo[0]][lo[1]] ==1:
        lo[0] -=di[s][0]
        lo[1] -=di[s][1]
        cnt +=1
        s +=1
        s %=4
    else:
        mat[lo[0]][lo[1]] ==1
        res +=1
        if cnt ==4:
            break

print(res)