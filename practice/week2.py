# 실습문제 1번: 면적/둘레 구하기
radius = int(input("원의 반지름을 입력하세요: "))
circum = 2 * 3.14 * radius
area = 3.14 * radius * radius

print("원의 둘레: {:.2f}".format(circum))
print("원의 넓이: {:.2f}".format(area))

# 실습문제 2번: 계산기 만들기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("{} + {} = {}".format(num1, num2, add))
print("{} - {} = {}".format(num1, num2, sub))
print("{} * {} = {}".format(num1, num2, mul))
print("{} / {} = {:.3f}".format(num1, num2, div))

# 실습문제 3번: 나이 계산
name = input("이름을 입력하세요: ")
print("{} 님, 파이썬 수업 수강을 환영합니다.".format(name))

now_year = int(input("올해의 연도를 입력하세요: "))
birth_year = int(input("태어나신 연도를 입력하세요: "))
print("{} 님은 한국 나이로 {}살이시군요.".format(name, now_year - birth_year))

# 실습문제 4번: 출력 양식
# 방법 1
num = int(input("정수를 입력하세요: "))

print("정수: ", int(num))
print("실수: ", float(num))
print("문자열: ", str(num))
print("2진수: ", bin(num))
print("8진수: ", oct(num))
print("16진수: ", hex(num))

# 방법 2
num = int(input("정수를 입력하세요: "))

print("정수: {}".format(num))
print("실수: {:.2f}".format(num))
print("문자열: {}".format(str(num)))
print("2진수: {0:b}".format(num))
print("8진수: {0:o}".format(num))
print("16진수: {0:x}".format(num))

# 출력 양식: format
year = 2024
month = 4
day = 3
day_week = '수'
temp = 13.5

# 방법 1
print("{}년 {}월 {}일은 {}요일입니다.".format(year, month, day, day_week))
print("한국식 표현 (년/월/일/요일): {0}/{1}/{2}/{3}".format(year, month, day, day_week))
print("미국식 표현 (년/월/일/요일): {3}/{1}/{2}/{0}".format(year, month, day, day_week))
print("영국식 표현 (년/월/일/요일): {3}/{2}/{1}/{0}".format(year, month, day, day_week))


# 방법 2
print("{y}년 {m}월 {d}일은 {dw}요일입니다.".format(y = year, m = month, d = day, dw = day_week))

# 방법 3
# m:02d -> 변수 m을 빈칸은 0으로 채우고 2자릿수까지 정수 형태로 출력
print("{y}년 {m:02d}월 {d}일은 {dw}요일입니다.".format(y = year, m = month, d = day, dw = day_week))
print("{0:02d}월 {1:02d}일은 {2}요일은 온도가 {3:.2f}도입니다.".format(month, day, day_week, temp))

# 출력 양식: format 함수의 정렬
num = 12345
print("출력 연습: 0000000000")

# 방법 1
print("좌측 정렬: {0:<10}".format(num))
print("중앙 정렬: {0:^10}".format(num))
print("우측 정렬: {0:>10}".format(num))

# 방법 2
print("좌측 정렬: {0:*<10}".format(num))
print("중앙 정렬: {0:*^10}".format(num))
print("우측 정렬: {0:*>10}".format(num))

# 실습문제 5번: 출력 양식
# 방법 1
print(f"{'*' * 5:>10}")
print(f"{'*' * 5:^10}")
print(f"{'*' * 5:<10}")

# 빙법 2
star = "*****"
print("{0:>10}".format(star))
print("{0:^10}".format(star))
print("{0:<10}".format(star))