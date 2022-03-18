# 1. 모험가 길드
# n = int(input())
# li = list(map(int, input().split()))
# li.sort()
# cnt = 0
# tem = 1
# for i in range(n):
#     if li[i] == tem:
#         tem =1
#         cnt +=1
#     elif li[i] > tem:
#         tem +=1
#         pass
# print(cnt)
    
'''
리뷰 : 단순한 구조로 이뤄져서 문제 풀이가 어려운점은 없었다.
'''

# 2. 곱하기 혹은 더하기
# txt = input()
# txt2 = 1
# for i in txt:
#     if i != '0':
#         txt2 *=int(i)
# print(txt2)
'''
리뷰 : 간단하다 생각되는 문제
'''

# 3. 문자열 뒤집기
# txt = input()
# txt2 = ''
# for i in range(len(txt)-1):
#     if txt[i] !=txt[i+1]:
#         txt2 +=txt[i]
# if txt2[-1] != txt[-1]:
#     txt2 += txt[-1]
# print(min(txt2.count('0'), txt2.count('1')))

# 4. 만들 수 없는 금액
# from itertools import combinations
# n = int(input())
# li = list(map(int, input().split()))

# li2 = []
# for i in range(2, n+1):
#     li2.append(list(combinations(li, i)))
# tem = []
# tem2 = []
# res = set(li)
# for j in li2:
#     tem =j
#     for k in tem:
#         tem2.append(k)
    
# for l in tem2:
#     res.add(sum(l))
# print(res)
# i = 1
# while True:
#     if not i in res:
#         break
#     i +=1
# print(i)

'''
리뷰 : 조합으로 해야된다는건 알고있었는데 조합 함수가 생각안나서 고민하다가
함수 있다는거 기억하고 바로 풀 수 있었다!
'''



# 5. 볼링공 고르기
# from itertools import combinations
# n, m = map(int, input().split())
# li = list(map(int, input().split()))
# dic = {i+1:j for i,j in enumerate(li)}

# res = list(combinations(dic.keys(), 2))
# res2 = []
# for i in range(len(res)):
#     if dic[res[i][0]] != dic[res[i][1]]:
#         res2.append(res[i])
# print(res2)
# print(len(res2))

'''
리뷰 : 알고만 있고 쓰지않던 combinations 함수를 처음으로 써봤는데 문제 풀이가
훨씬 깔끔해짐을 알 수 있었다.
'''

# 6. 무지의 먹방 라이브

# def solution(food_times, k):
#     answer = 0
#     i = 0
#     clear = False
#     while True:
#         if (k == 0) or (clear ==True):
#             break
#         if food_times[i]==0:
#             i +=1
#             i %=len(food_times) # 인덱스
#         else:
#             food_times[i] -=1
#             k -=1
#             i+=1
#             i %=len(food_times)
#             if sum(food_times) == 0:
#                 clear = True
#     if clear == True:
#         answer = -1
#     else:
#         answer = i+1
#     return answer

'''
정확성: 28.1
효율성: 0.0
합계: 28.1 / 100.0
'''

from math import radians


def solution(food_times, k):
    answer = 1
    dic = {j+1: t for j,t in enumerate(food_times)}
    le = len(food_times)
    r = len(food_times)
    for _ in range(k):
        if le == 0:
            answer = -1
            break
        while True:
            if dic[answer] !=0:
                dic[answer] -=1
                le -=1
                answer +=1
                answer %=(r + 1)
                break
            else:
                answer +=1        
                answer %=(r + 1) 
    if answer != -1:
        while True:     
            if dic[answer] !=0:
                answer +=1
                answer %=(r + 1)
                break
            else:
                answer +=1        
                answer %=(r + 1) 
    return answer

print(solution([3, 1, 2],5))