# 1010번 다리놓기
'''

'''
import math
tc = int(input())
for _ in range(tc):
    n,m=map(int, input().split())
    print(math.comb(m,n))
