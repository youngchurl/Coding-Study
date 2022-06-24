'''# 14425 문자열 집합
n, m = map(int, input().split())
li = []
cnt = 0
for _ in range(n):
    li.append(input())
for _ in range(m):
    test = input()
    if test in li:
        cnt +=1
print(cnt)'''

# 1269 대칭 차집합
'''n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a-b
d = b-a
res = len(c)+len(d)
print(res)'''

# 11478 서로 다른 부분 문자열의 개수

'''text = input()
le = len(text)
res = set()
for i in range(le):
    for j in range(1,le):
        res.add(text[i:i+j])
print(len(res)+1)'''

# 2477 참외밭

k = int(input())
