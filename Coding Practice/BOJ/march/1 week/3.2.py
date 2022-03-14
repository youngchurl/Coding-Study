# 백준 1439 뒤집기
# 그리디 [7]

txt = input()
cnt = [0,0] # 0 count, 1 count

for i in range(1,len(txt)):
    if txt[i] == '0' and txt[i-1] =='1':
        cnt[0] +=1
    elif txt[i] == '1' and txt[i-1] =='0':
        cnt[1] +=1

if cnt[0] !=0 and cnt[1] !=0:
    if txt[0] == '0':
        cnt[0] +=1
    else :
        cnt[1] +=1

cnt.sort()

if cnt[0] == 0 and cnt[1] == 0:
    print("0")
elif cnt[0] == 0:
    print(cnt[1])
elif cnt[0] != 0:
    print(cnt[0])   
   
# 한줄평 : 하는 방법은 문제를 읽자마자 알았지만, 은근 생각해야될 부분이 많아서 바로 풀리진 않고 좀 고민했어야 하는 문제 였다!!
