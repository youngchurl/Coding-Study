# 2072 홀수만 더하기
#  
testcase = int(input())
for _ in range(1,testcase+1):
    n = list(map(int, input().split())) # 공백으로 나눠서 리스트안에 넣기
    num = [_ for _ in n if _%2 !=0] # num 안에 홀수만 담기
    print(f"#{_} {sum(num)}")

# 1859 백만 장자 프로젝트 / 실패
T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    #배열을 뒤집음
    arr = arr[::-1]
    #첫 원소를 최대값으로 저장
    max_v = arr[0]
    cnt = 0
    for i in range(1,len(arr)):
    	#최대값보다 작은 값이면 이득을 본 것으로 계산
        if max_v > arr[i]:
            cnt += max_v-arr[i]
        #최대값보다 더 큰 값이면 새로운 최대값으로 저장
        else:
            max_v = arr[i]
    print("#{} {}".format(t, cnt))

# 1204 SW 문제해결 기본 1일차 - 최빈수 구하기
from collections import Counter

T = int(input()) # 테스트 케이스 입력

for _ in range(T):
    n = int(input()) # 테스트 케이스 번호
    arr = list(map(int, input().split())) # 입력값 입력 
    arr.sort(reverse=True) # 높은 점수 -> 낮은 점수 순으로 배열

    count = Counter(arr).most_common(1) # 최빈값중 최고 점수 하나를 count에 입력

    print(f'#{n} {count[0][0]}') # 2차원 배열 형태이므로 [][]로 꺼낸다.    
    
    
    
2 주차 

# 2022.01.30

# SW 2050 알파벳을 숫자로 변환

text = input() # 문자열을 받는다.
text2 = text.upper() # 소문자가 있을 수 있으니 대문자로 전부 치환한다.
text_li = [] # 아스키코드 변환 후 담을 리스트 생성

for i in range(len(text)):
    text_li.append(ord(text2[i])-64) # 아스키 코드가 A 65 이렇게 시작을 하기 때문에 64를 빼준다.

for _ in text_li: print(_,end=" ") # 배열 출력
    
   
# SW 1966번 숫자를 정렬하자.

T = int(input()) # 테스트 케이스 입력받음

for i in range(1,T+1):
    n = int(input()) # 리스트 내 숫자 개수 
    num_li = list(map(int, input().split())) # 리스트로 숫자를 받는다.
    num_li.sort() # 낮은 순서대로 배열


    print(f"#{i}",*num_li) # 출력

