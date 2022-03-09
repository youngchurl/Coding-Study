# 1966번 프린터 큐
import sys
input = sys.stdin.readline

al = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i in range(len(al)):
    dic[al[i]] =i+1

n = int(input().rstrip())
txt = input().rstrip()
res = 0
for i in range(n):
    res += (31**i)*dic[txt[i]]
print(res%1234567891)


'''
리뷰 : 모드를 생각안해서 계속 50점이 나왔는데 모드까지 생각을 하고나니
쉽게 풀 수 있던 문제였다.
'''