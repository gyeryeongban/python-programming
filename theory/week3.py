# 나눗셈
print(7 / 4)
print(7 // 4)

# 나머지 연산자
p = int(input("분자를 입력하시오: "))
q = int(input("분모를 입력하시오: "))
print("나눗셈의 몫 =", p // q)
print("나눗셈의 나머지 =", p % q)

# 나머지 연산자의 용도
number = int(input("정수를 입력하시오: "))
print(number%2)

# 나머지 연산자의 용도
sec = 1000
min = 1000 // 60
remainder = 1000 % 60
print(min, remainder)

# Lab: 커피 가게 매출 계산하기
ameriPri = 2000
cafelaPri = 3000
cappuPri = 3500

ameriNum = int(input("아메리카노 판매 개수: "))
cafelaNum = int(input("카페라떼 판매 개수: "))
cappuNum = int(input("카푸치노 판매 개수: "))

sum = (ameriPri * ameriNum) + (cafelaPri * cafelaNum) + (cappuPri * cappuNum)
print("총 매출은 {}입니다.".format(sum))

# 도전 문제
total = 100000

if sum > total:
    print("흑자")
else:
    print("적자")

# Lab: 화씨 온도를 섭씨 온도로 변환하기
f = int(input("화씨 온도: "))
c = (f - 32) * 5/9
print("섭씨 온도: ", c)

# 도전 문제
c = int(input("섭씨 온도: "))
f = c * 9/5 + 32
print("화씨 온도: ", f)

# Lab: BMI 계산하기
kg = float(input("몸무게를 kg 단위로 입력하시오: "))
cm = float(input("키를 미터 단위로 입력하시오: "))
bmi = kg / cm ** 2
print("당신의 BMI = ", bmi)

# Lab: 자동 판매기 프로그램 1
money = int(input("투입한 돈: "))
price = int(input("물건 값: "))
change = money - price
print("거스름돈: ", change)

coin500 = change // 500
change = change % 500
coin100 = change // 100
print("500원 동전의 개수: ", coin500)
print("100원 동전의 개수: ", coin100)

# 도전 문제
change = change % 100
coin50 = change // 50
change = change % 50
coin10 = change // 10
print("50원 동전의 개수: ", coin50)
print("10원 동전의 개수: ", coin10)

# 지수 계산
print(2 ** 7)

a = 1000
r = 0.05
n = 10
pi = a * (1 + r) ** n
print(pi)

# 복합 연산자
x = 1000
print("초기 값 X = ", x)
x += 2
print("x += 2 후의 X =", x)
x -= 2
print("x -= 2 후의 X =", x)

# 괄호의 사용
print(10 + 20 / 2)
print((10 + 20) / 2)

# Lab: 평균 구하기
x = int(input("첫 번째 수를 입력하시오: "))
y = int(input("두 번째 수를 입력하시오: "))
z = int(input("세 번째 수를 입력하시오: "))
avg = (x + y + z) / 3
print("평균 = ", avg)

# 관계 연산자
a, b = 100, 200
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# 논리 연산자
a = 99
print((a > 100) and (a < 200))
print((a > 100) or (a < 200))
print(not(a == 100))

# 비트 연산자
# 비트 논리곱(&) 연산자
print(10 & 7)
print(123 & 456)
print(0xFFFF & 0x0000)

# 비트 논리합(|) 연산자
print(10 | 7)
print(123 | 456)
print(0xFFFF | 0x0000)

# 비트 배타적 논리합(^) 연산자
print(10 ^ 7)
print(123 ^ 456)
print(0xFFFF ^ 0x0000)

# 비트 부정(~) 연산자
a = 12345
print(~a + 1)

# 왼쪽 시프트(<<) 연산자
a = 10
print(a << 1, a << 2, a << 3, a << 4)

# 오른쪽 시프트(>>) 연산자
a = 10
print(a >> 1, a >> 2, a >> 3, a >> 4)