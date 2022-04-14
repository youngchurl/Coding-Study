# 9237번 이장님 초대
'''
4 3 2 1 0
0 3 2 1 0
0 0 3 2 1 0
0 0 0 2 1 0
'''
n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
day = li[0]+1
cnt = 0
for i in li:
    cnt +=1
    day -=1
    if day<i:
        day = i
print(day + cnt+1)

'''
리뷰 : 간만에 풀어보는 그리디 문제였지만 실버 5라 그런지 그렇게 어렵지 않았다!
'''