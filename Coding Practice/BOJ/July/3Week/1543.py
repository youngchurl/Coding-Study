# 1543번 문서 검색
te = input()
ea = input()
cnt = 0
i = 0
le = len(ea)

while i<len(te):
    if te[i:i+le] == ea:
        cnt +=1
        # print(te)
        te = te[i+le:]
        i = 0
    else:
        i +=1

print(cnt)