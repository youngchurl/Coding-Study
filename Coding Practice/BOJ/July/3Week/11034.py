# 11034 캥거루 세마리2
while True:
    try:
        a,b,c = map(int, input().split())
        res1 = b-a
        res2 = c-b
        print(max(res2, res1)-1)
    except:
        exit()