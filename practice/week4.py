# 실습문제 1: 복소수 계산
num1 = 2.7 + 3.2j
num2 = 5.1 -2.6j
sum = (2.7 + 3.2j) + (5.1 -2.6j)
sub = (2.7 + 3.2j) - (5.1 -2.6j)
mul = (2.7 + 3.2j) * (5.1 -2.6j)

print("덧셈 결과: {:.2f}".format(sum))
print("뺄셈 결과: {:.2f}".format(sub))
print("곱셈 결과: {:.2f}".format(mul))
print("2.7 + 3.2j 복소수의 실수 부분:", num1.real)
print("2.7 + 3.2j 복소수의 허수 부분:", num1.imag)
print("5.1 -2.6j 복소수의 켤레복소수:", num2.conjugate())
print("5.1 -2.6j 복소수의 크기: {:.2f}".format(abs(num2)))

# 실습문제 2: 오늘 날짜 및 시간
import time

now = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", now))

year = now.tm_year
month = now.tm_mon
day = now.tm_mday
hour = now.tm_hour
minute = now.tm_min

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))
print("현재 시간은 {}시 {}분입니다.".format(hour, minute))

korea = time.strftime("%Y/%m/%d", now)
us = time.strftime("%m/%d/%Y", now)
uk = time.strftime("%d/%m/%Y", now)

print("한국식 표현(년/월/일):", korea)
print("미국식 표현(월/일/년):", us)
print("영국식 표현(일/월/년):", uk)

# 오늘 날짜와 현재 시간
import datetime

dt_now = datetime.datetime.now()
print(dt_now)

print(dt_now.date()) # 날짜
print(dt_now.year) # 연도
print(dt_now.month) # 월
print(dt_now.day) # 일
print(dt_now.time()) # 시간
print(dt_now.hour) # 시
print(dt_now.minute) # 분
print(dt_now.second) # 초

today = datetime.datetime.today()
print("오늘은 {0}년 {1:02d}월 {2:02d}일입니다.".format(today.year, today.month, today.day))

d_day = today + datetime.timedelta(days = 100)
print("100일 후는 {0}년 {1:02d}월 {2:02d}일입니다.".format(d_day.year, d_day.month, d_day.day))

# 실습문제 3: 출생 후 경과일 계산
birthYear = int(input("출생년도를 입력하세요: "))
birthMonth = int(input("출생월을 입력하세요: "))
birthDay = int(input("출생일을 입력하세요: "))

birthday = datetime.date(birthYear, birthMonth, birthDay)
today = datetime.date.today()
passed = (today - birthday).days

print("출생일({}년 {}월 {}일)로부터 {}일 지났습니다.".format(birthYear, birthMonth, birthDay, passed))

# 실습문제 4: 날짜 계산
import datetime

after = int(input("오늘로부터 며칠 후를 알고 싶으신가요? "))

today = datetime.datetime.today()
print("오늘은 {0}년 {1:02d}월 {2:02d}일입니다.".format(today.year, today.month, today.day))

afterDay = today + datetime.timedelta(days = after)
print("{}일 후는 {}년 {}월 {}일입니다.".format(after, afterDay.year, afterDay.month, afterDay.day))

# 실습문제 4: 개인정보
impor = []

name = input("당신의 이름은? ")
impor.append(name)

age = int(input("당신의 나이는? "))
impor.append(age)

height = float(input("당신의 키는? "))
impor.append(height)

print(impor)
print("안녕하세요 {}님.".format(impor[0]))
print("2050년에는 {}살이 되시겠네요.".format((2050 - 2024) + impor[1]))

maleSub = 175.5 - height
femaleSub = 163.2 - height

print("남자 평균 키인 175.5cm에 {:.2f}cm, 여성 평균 키인 163.2cm에 {:.2f}cm 차이가 나네요.".format(maleSub, femaleSub))

# 실습문제 5: 총합 평균 구하기
num1 = int(input("정수를 입력하시오: "))
num2 = int(input("정수를 입력하시오: "))
num3 = int(input("정수를 입력하시오: "))
num4 = int(input("정수를 입력하시오: "))
num5 = int(input("정수를 입력하시오: "))

list = [num1, num2, num3, num4, num5]
print(list)

sum = num1 + num2 + num3 + num4 + num5
aver = (num1 + num2 + num3 + num4 + num5) / 5
print("데이터 합계:", sum)
print("데이터 평균: {:.2f}".format(aver))