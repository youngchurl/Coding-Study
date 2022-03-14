# SW 1970 쉬운 거스름돈

money = [50000,10000,5000,1000,500,100,50,10]
tc = int(input())

for i in range(1,tc+1):
    pay = int(input())
    mon = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(8):
        if pay>= money[j]:
            m = pay//money[j]
            pay -= (m*money[j])
            mon[j] += m
        
    print(f'#{i}')
    print(*mon)

# 한줄평 : 처음에 매번 mon을 초기화 하는걸 설계를 안해서 값이 안나왔지만 문제 자체는 
# 표준 그리디 문제라서 어려움이 없었다.
