# 실습문제 1: 평균 키 판별
gender = input("성별을 입력하시오 (M/m/F/f): ")
height = float(input("키를 입력하시오: "))
female = 163.2
male = 173.5

if gender.lower() == "f":
    if height >= female:
        print("한국 여성의 평균 키 이상입니다.")
    else:
        print("한국 여성의 평균 키 미만입니다.")
elif gender.lower() == "m":
    if height >= male:
        print("한국 남성의 평균 키 이상입니다.")
    else:
        print("한국 남성의 평균 키 미만입니다.")
else:
    print("M/m/F/f 중 하나를 입력하시오.")

# 실습문제 2: 4와 5의 배수 (if문)
num = int(input("숫자를 입력하세요: "))

if num % 4 == 0 and num % 5 == 0:
    print(num, "은 4의 배수이면서 5의 배수입니다.")
elif num % 4 == 0 and num % 5 != 0:
    print(num, "은 4의 배수이지만 5의 배수가 아닙니다.")
elif num % 4 != 0 and num % 5 == 0:
    print(num, "은 5의 배수이지만 4의 배수가 아닙니다.")
else:
    print(num, "은 4의 배수도 아니고 5의 배수도 아닙니다.")

# 실습문제 3: 놀이기구 탑승 1 (if-else문)
age = int(input("나이를 입력하세요: "))
height = int(input("키를 입력하세요: "))

if age >= 10 and height >= 165:
    print("놀이기구를 이용할 수 있습니다.")
else:
    print("놀이기구를 이용할 수 없습니다.")

# 실습문제 4: 놀이기구 탑승 2 (if-else문)
age = int(input("나이를 입력하세요: "))
height = int(input("키를 입력하세요: "))

if age >= 10 and height >= 165:
    print("{}살이고 {}cm 키는 놀이기구를 이용할 수 있습니다.".format(age, height))
elif age < 10 and height >= 165:
    print("{}살은 놀이기구를 이용할 수 없습니다.".format(age))
elif age >= 10 and height < 165:
    print("{}cm 키는 놀이기구를 이용할 수 없습니다.".format(height))
else:
    print("놀이기구를 이용할 수 없습니다.")

# 실습문제 5: 날짜 및 시간 출력 (if-elif-else문)
import datetime

now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 0:
    weekdayStr = "월요일"
elif weekday == 1:
    weekdayStr = "화요일"
elif weekday == 2:
    weekdayStr = "수요일"
elif weekday == 3:
    weekdayStr = "목요일"
elif weekday == 4:
    weekdayStr = "금요일"
elif weekday == 5:
    weekdayStr = "토요일"
elif weekday == 6:
    weekdayStr = "일요일"

if now.hour < 12:
    hourStr = "오전"
else:
    hourStr = "오후"

hour = now.hour % 12

if hour == 0:
    hour = 12

print("지금은 {}년 {}월 {}일 {} {} {}시 {}분입니다.".format(now.year, now.month, now.day, weekdayStr, hourStr, hour, now.minute))

# 실습문제 6: 성적 처리 (if-elif-else문)
python = int(input("파이썬 점수를 입력하세요: "))
c = int(input("C언어 점수를 입력하세요: "))
computer = int(input("컴퓨터개론 점수를 입력하세요: "))

sum = python + c + computer
average = sum / 3

print("총점:", sum)
print("평균: {:.2f}".format(average))

if average >= 90 and average <= 100:
    print("A학점입니다.")
    print("성적 우수 장학생입니다.")
elif average >= 80 and average < 90:
    print("A학점입니다.")
    print("우수한 성적입니다.")
elif average >= 70 and average < 80:
    print("C학점입니다.")
    print("조금 더 노력해야 합니다.")
elif average >= 60 and average < 70:
    print("D학점입니다.")
    print("열심히 노력해야 합니다.")
elif average < 60:
    print("F학점입니다.")
    print("다음에 재수강해야 합니다.")