# 2.24
# 7568번 덩치

num = int(input())
li= []
res = [1]*num

for _ in range(num):
    li.append(list(map(int,input().split())))

for i in range(num):
    for j in range(num):
        if li[i][0] <li[j][0] and li[i][1] <li[j][1]:
            res[i] +=1

print(*res)

# 한줄평 : 2중 for 문을 이용해서 풀면 굉장히 쉬운 문제였는데, 다르게 더 좋은 방법은 생각나지가 않는다...
