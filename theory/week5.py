# 예제 1
score = int(input("성적을 입력하시오: "))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

# 예제 2
num = int(input("정수를 입력하시오: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# Lab: 영화 나이 제한 검사
age = int(input("나이를 입력하시오: "))
if age >= 15:
    print("이 영화를 보실 수 있습니다.")
    print("영화의 가격은 10000원입니다.")

else:
    print("이 영화를 보실 수 없습니다.")
    print("다른 영화를 보시겠어요?")

# Lab: 윤년 판단
year = int(input("연도를 입력하시오: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")

# Lab: 동전 던지기 게임
import random
print("동전 던지기 게임을 시작합니다.")
if random.randrange(2) == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")

# if-elif-else문
num = int(input("정수를 입력하시오: "))

if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")

# Lab: 종달새가 노래할까?
import random
time = random.randint(1, 24)
print("좋은 아침입니다. 지금 시각은 {}시입니다.".format(time))

sunny = random.choice([True, False])
if sunny:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

if (time >= 6 and time <= 9) and (time >= 14 and time <= 16) and sunny:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")

# 예제 3
num = int(input("정수를 입력하시오: "))
if num >= 0:
    if num == 0:
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")

# Lab: 로그인 프로그램
id = "ilovepython"
inputId = input("아이디를 입력하시오: ")
password = "123456"
inputPassword = input("비밀번호를 입력하시오: ")

if id == inputId and password == inputPassword:
    print("환영합니다.")
else:
    print("아이디 또는 비밀번호를 찾을 수 없습니다.")

# Lab: 축구 게임
defend = ["왼쪽 상단", "왼쪽 하단", "중앙", "오른쪽 상단", "오른쪽 하단"]
computer = random.choice(defend)
user = input("어디를 수비하시겠어요? (왼쪽 상단, 왼쪽 하단, 중앙, 오른쪽 상단, 오른쪽 하단) ")

if computer == user:
    print("수비에 성공하셨습니다.")
else:
    print("페널티 킥이 성공하였습니다.")

# Lab: 직각삼각형 판별
a = int(input("변 a의 길이: "))
b = int(input("변 b의 길이: "))
c = int(input("변 c의 길이: "))

if a**2 + b**2 == c**2:
    print("직각삼각형입니다.")
else:
    print("직각삼각형이 아닙니다.")

# Lab: 사분면 판단
x = int(input("x 좌표를 입력하시오: "))
y = int(input("y 좌표를 입력하시오: "))

if x > 0 and y > 0:
    print("1사분면입니다.")
elif x < 0 and y > 0:
    print("2사분면입니다.")
elif x < 0 and y < 0:
    print("2사분면입니다.")
else:
    print("4사분면입니다.")