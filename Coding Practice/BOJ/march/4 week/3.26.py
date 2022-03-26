# 1. Boj 18870번 좌표 압축
# n = int(input())
# li = list(map(int, input().split()))
# tem = sorted(list(set(li)))
# dic = {i:j for j,i in enumerate(tem)}

# for i in li:
#     print(dic[i], end=' ')

'''
리뷰 : 딕셔너리로 바로 풀려서 뿌듯했다.
'''

# 2. Boj 9663번 N-Queen
n = int(input())
if n <=3:
    print('0')
else:
    res = 2*4**(n-4)
    print(res)