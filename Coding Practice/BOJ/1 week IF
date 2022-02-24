# 2022.01.21
# 백준 1330 두수 비교하기 
a, b = map(int, input().split()) # 두 수를 공백으로 구분 짓고 한번에 입력 받는다.
if a > b : 
    print(">") # A > B 이기 때문에 > 출력
elif a == b : 
    print("==") # A == B 이기 때문에 == 출력
else : 
    print("<") # 남은 경우의 수는 전부 < 로 출력해도 무방하다.

# 백준 9498 시험성적
score = int(input()) # 시험점수를 입력 받는다.
if score >= 90:
    print("A") # 90 ~ 100 점 A 
elif score >= 80:
    print("B") # 80 ~ 89점 B
elif score >= 70:
    print("C") # 70 ~ 79점 C
elif score >= 60:
    print("D") # 60 ~ 69점 D
else :
    print("F") # 나머지 점수 F


# 2022.01.22

# 백준 2753번 윤년
year = int(input()) # 연도를 입력 받는다.

if year % 400 == 0 : # 400의 배수일 때 윤년 o 
    print('1')
elif year % 100 == 0 : # 100의 배수는 윤년 x
    print('0') 
elif year % 4 == 0 : # 4의 배수는 윤년 o
    print('1')
else : 
    print('0')


# 백준 14681번 사분면 고르기
x = int(input()) # x 좌표값 입력
y = int(input()) # y 좌표값 입력

if x > 0 and y > 0: # x, y 둘다 양수
    print('1')
elif x > 0 and y < 0: # x 양수, y 음수
    print('4')
elif x < 0 and y > 0: # x 음수, y 양수
    print('2')
elif x < 0 and y < 0 :
    print("3")

# 백준 2884번 알람시계

H, M = map(int, input().split())

if M >= 45 : # 45분 이상이라면 시간의 변동이 없다. 
    print(f"{H} {M-45}") 
else:
    if H==0: # 시간이 0시라면 23시가 되니 예외로 먼저 빼둔다.
        print(f"23 {M+15}") # 60+M-45=M+15
    else:
        print(f"{H-1} {M+15}")


https://www.acmicpc.net/step/4
