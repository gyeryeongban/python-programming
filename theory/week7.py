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