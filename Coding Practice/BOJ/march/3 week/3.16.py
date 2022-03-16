# 1. 11723번 집합
# import sys
# input = sys.stdin.readline
# s = set()
# for _ in range(int(input().rstrip())):
#     order = input().strip().split()

#     if len(order) == 1 :
#         if order == 'all':
#             s = set([i for i in range(1,21)])
#         else:
#             s = set()

#     else:
#         o, n = order[0], order[1]
#         n = int(n)
#         if o == 'add':
#             s.add(n)
#         elif o == 'remove':
#             s.discard(n)
#         elif o == 'check':
#             if n in s:
#                 print('1')
#             else:
#                 print('0')
#         else:
#             if n in s:
#                 s.discard(n)
#             else:
#                 s.add(n)

'''
리뷰 : 비트 마스킹 이라는 스킬이 있다는걸 처음 알았기도 하고
세트가 있다는걸 자꾸 까먹어서 문제다.. 딕셔너리로 구현했었는데... 아쉽다.
'''
# 2. 1620번 나는야 포켓몬 마스터 이다솜
# import sys
# n, m =map(int, sys.stdin.readline().rstrip().split())
# li = [sys.stdin.readline().rstrip() for _ in range(n)]
# dic = {str(i+1) : j for i,j in enumerate(li)}
# dic2 = {j:i for i,j in dic.items()}

# for i in range(m):
#     res = sys.stdin.readline().rstrip()
#     if res[0] in '0123456789':
#         print(dic[res])
#     else:
#         print(dic2[res])

'''
리뷰 : 딕셔너리를 이렇게 써도 될지는 모르겠는데 키, 밸류 뒤집는 스킬을
새롭게 익힐 수 있어서 좋았다.
'''
# 3. 1676번 팩토리얼 0의 개수

# num = int(input())
# res = 1
# for i in range(1,num+1):
#     res *=i
# res = str(res)
# res = res[::-1]
# cnt = 0
# for j in res:
#     if j != '0':
#         break
#     cnt+=1
# print(cnt)

'''
리뷰 : 최근에 시간초과로 하도 혼나서 이 문제도 보자마자 시간초과가 겁났었는데
제약이 없어서 굉장히 쉬웠던 문제다.
재귀로 풀까 하다가 시간 초과가 걱정되서 for문으로 풀었다. 
'''

# 4. 1764번 듣보잡
# import sys
# h, w =map(int, sys.stdin.readline().rstrip().split())
# dic = {}
# res = []
# cnt = 0

# for _ in range(h):
#     o = sys.stdin.readline().rstrip()
#     dic.setdefault(o,0)
# for _ in range(w):
#     o = sys.stdin.readline().rstrip()
#     if o in dic.keys():
#         res.append(o)
#         cnt +=1
# print(cnt)
# res.sort()
# for i in res:
#     print(i)

'''
리뷰 : 사전순 이라는 단어를 못봐서 혼자 엄청 고민했다... 난이도 자체는 
크게 어렵지 않았다.
'''

# 5. 1003번 피보나치 함수
# 첫번째 풀이 - 일반 풀이
'''import sys
def fi(n):
    global cnt
    global cnt2
    if n ==0:
        cnt +=1
        return 0
    elif n ==1:
        cnt2 +=1
        return 1
    else:
        return fi(n-1) + fi(n-2)

for _ in range(int(sys.stdin.readline().rstrip())):
    cnt = 0
    cnt2 = 0
    n = int(sys.stdin.readline().rstrip())
    print(fi(n))
    print(cnt, cnt2)'''

# 두번째 풀이 동적 프로그래밍

# import sys
# for _ in range(int(sys.stdin.readline().rstrip())):
#     n = int(sys.stdin.readline().rstrip())
#     res1 = [0]*50
#     res2 = [0]*50
#     res1[0] = 1
#     res1[1] = 0
#     res2[0] = 0
#     res2[1] = 1
#     if n == 0 :
#         print(1,0)
#     elif n == 1:
#         print(0,1)
#     else:
#         for i in range(2, n+1):
#             res1[i] = res1[i-1] + res1[i-2]
#             res2[i] = res2[i-1] + res2[i-2]
#         print(res1[n], res2[n])

'''
리뷰 : 동적 프로그래밍 해야지 해야지 하면서 미루고 있었는데...
이렇게 문제로 바로 만날줄은 생각도 못했다.. 어쩐지 시간초과로 절대 안풀리던게
동적 프로그래밍을 적용하니깐 쉽게 풀렸다.
'''

# 6. 17219번 비밀번호 찾기
# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# dic = {}
# for _ in range(n):
#     txt = input().rstrip().split()
#     key = txt[0]
#     val = txt[1]
#     dic.setdefault(key, val)

# for _ in range(m):
#     res = input().rstrip()
#     print(dic[res])

'''
리뷰 : 그냥 무난하게 풀 수 있던 문제
'''

n = int(input())
li = [1,2,3,4,2,3,4,3,4,4]
i = -1
for _ in range(n):
    i+=1
    i%=10

print(li[i])