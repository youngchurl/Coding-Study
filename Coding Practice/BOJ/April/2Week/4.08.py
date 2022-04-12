# 1. Boj 수정렬하기 3 
import sys
input = sys.stdin.readline
tc = int(input())
dic = {i:0 for i in range(1,10001)}
for i in range(tc):
    a = int(input())
    dic[a] +=1
for i in range(1,10001):
    if dic[i] !=0:
        for j in range(dic[i]):
            print(i)