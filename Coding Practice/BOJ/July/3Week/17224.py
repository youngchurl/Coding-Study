# 17224 APC는 왜 서브테스크 대회가 되었을까?

n, l, k = map(int, input().split())
easy = 0
hard = 0
res = 0
for _ in range(n):
    a,b = map(int, input().split())
    if a<=l:
        if b<=l:
            hard +=1
        else:
            easy +=1

if hard >= k:
    res = k*140
else:
    
    res = hard*140 + min((k-hard), easy)*100
print(res)