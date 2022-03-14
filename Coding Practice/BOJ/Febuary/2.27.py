# 백준 11047 동전 0 

n , k = map(int, input().split())
li = [] # 동전 집어 넣을 리스트
res = 0 # 동전 개수 최소값

for i in range(n):
    li.append(int(input()))

for j in range(1,n+1):
    if li[-j]<= k: # 거꾸로 비교하면서 동전으로 치환 되는지 비교
        n= k//li[-j] # 동전이 몇개가 들어가는지 개수 파악
        k %=li[-j] # 해당 동전으로 나누고 나머지를 k로 남겨줌
        res+=n # 몇개 들어가는지 파악 후 동전 개수 집어 넣음

print(res)

# 한줄평 : 생각한대로 구현했는데 바로 구현이 되서 기분 좋았다! 별다른 어려운 개념은 들어가지 않았다.
