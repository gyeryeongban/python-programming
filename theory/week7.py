# 1000번 반복
for i in range(1000):
    print("방문을 환영합니다!")

# 횟수 제어 반복
for i in [1, 2, 3, 4, 5]:
    print("방문을 환영합니다.")

# i의 값 출력
for i in [1, 2, 3, 4, 5]:
    print("i=", i)

# 구구단 출력
for i in [1, 2, 3, 4, 5]:
    print("9 *", i, "=", 9*i)

# range() 함수
for i in range(5):
    print("방문을 환영합니다!")

for i in range(1, 6, 1):
    print(i, end=" ")

for i in range(10, 0, -1):
    print(i, end=" ")

# Lab: 1부터 100까지 합 계산하기
sum = 0
for i in range(1, 101, 1):
    sum += i
print("1부터 100까지의 합은 ", sum, "입니다.")

# Lab: 팩토리얼 계산하기
num = int(input("정수를 입력하시오: "))
mul = 1
for i in range(1, num+1):
    mul *= i
print("{}!은 {}이다.".format(num, mul))

# 예제 1
password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오: ")
print("로그인 성공")

# 예제 2
num = 1
sum = 0
while num <= 10:
    sum += num
    num += 1 # 숫자를 1씩 늘려줘야 함
print("합계는", sum)

# 중첩 반복문
for i in range(5):
    for j in range(10):
        print("*", end=" ")
    print("")

for j in range(1, 6):
    print("* " * j)
print("")

# 별 찍기
for i in range(4):
    print(" " * (4 - (i + 1)), end="")
    print("* " * (i + 1))

# 무한 반복문
sign = True

while sign:
    light = input("신호등 색상을 입력하시오: ")
    if light == "blue":
        sign = False

print("전진!")

# break와 continue
while True:
    light = input("신호등 색상을 입력하시오: ")
    if light == "blue":
        break
print("전진!")

for n in range(10):
    if n % 2 == 0:
        continue
    print(n)

# Lab: 구구단 출력
# for
dan = int(input("원하는 단은: "))

for i in range(1, 10):
    print("{} * {} = {}".format(dan, i, dan * i))

# while
dan = int(input("원하는 단은: "))
i = 1

while i <= 9:
    print("%s * %s = %s" % (dan, i , dan * i))
    i = i + 1

# 도전문제
for i in range(1, 10):
    for j in range(1, 10):
        print("%s * %s = %s" % (i, j, i * j))
    print("")

# Lab: 범인 찾기 게임
import random
score = 0

while True:
    room = random.randint(1, 3)
    choice = int(input("방 번호를 입력하시오: "))

    if room == choice:
        print("범인 체포!")
        score += 100
        break

    elif choice > 3:
        print(n, "번 방은 없습니다.")
    
    else:
        print("범인이 없습니다.")
        score -= 10

print("게임 종료")
print("점수:", score, "점")

# Lab: 약수 구하기
import random

tries = 1
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")
guess = int(input("숫자를 입력하시오: "))

while guess != answer:
    tries = tries + 1
    
    if guess < answer:
        print("낮음!")
    
    elif guess > answer:
        print("높음!")
    
    guess = int(input("숫자를 입력하시오: "))

if guess == answer:
    print("축하합니다. 시도 횟수 =", tries)