# 1049번 기타줄
'''
경우의 수 
1. 패키지만 사서 해결
2. 낱개만 사서 해결
3. 1,2 통합
'''
n, m = map(int,input().split())
pa = [] # 패키지 가격 저장
ea = [] # 낱개 가격 저장

for _ in range(m):
    a,b = map(int, input().split())
    pa.append(a)
    ea.append(b)

case1 = ((n//6) + 1)*min(pa)
case2 = n*min(ea)
case3 = min(pa)*(n//6) + (n%6)*min(ea)
print(min(case1, case2, case3))