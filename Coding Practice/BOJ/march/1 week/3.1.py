# 2022. 03. 01
# 1026번 보물
# 그리디 [4]
n = int(input())

a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))
a_li.sort() # 오름 차순 정렬
b_li.sort(reverse=True) # 내림 차순 정렬
res = 0

for i in range(n):
    res +=(a_li[i] * b_li[i])
print(res)

# 5585번 거스름돈
# 그리디 [5]
coin = [500, 100, 50, 10, 5, 1]

n = 1000 - int(input())
res = 0
for i in coin:
    if n>=i:
        m = n//i
        res +=m
        n -=(m*i)

print(res)

# 한줄평 : 이제는 자연스럽게 풀게되는 거스름돈 문제

# 10162번 전자레인지
# 그리디 [6] 
# 서브테스크 100점!

button = [300,60,10]
res = [0 for _ in range(3)]

n = int(input())
if n%10 !=0:
    print('-1')
else:
    for i in range(3):
        if n>=button[i]:
            m = n//button[i]
            res[i] +=m
            n -=m*button[i]

    print(*res)

# 한줄평 : 서브테스크 문제는 처음이었는데 백점 받을 수 있었다!
