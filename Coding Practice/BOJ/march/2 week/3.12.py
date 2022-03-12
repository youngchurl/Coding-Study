# 이코테 예제 3-1 거스름돈
# coin = [500, 100, 50, 10]
# money = int(input())
# cnt = 0
# for i in coin:
#     tem = money//i
#     money -= tem*i
#     cnt += tem

# print(cnt)

# 이코테 예제 3-2 큰 수의 법칙
n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
cnt = 1
res = 0
num = 0
for i in range(m):
    res +=li[num]
    cnt +=1
    if cnt ==3:
        num +=1
        cnt = 0
    if cnt == 1:
        num = 0
    
print(res)