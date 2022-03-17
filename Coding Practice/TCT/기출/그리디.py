# 1 모험가 길드
n = int(input())
li = list(map(int, input().split()))
li.sort()
cnt = 0
tem = 1
for i in range(n):
    if li[i] == tem:
        tem =1
        cnt +=1
    elif li[i] > tem:
        tem +=1
        pass
print(cnt)
    
'''
리뷰 : 단순한 구조로 이뤄져서 문제 풀이가 어려운점은 없었다.
'''

