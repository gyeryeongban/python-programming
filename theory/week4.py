# 복소수
x = 10 + 30j
print(x)
print(type(x))

# 문자열 -> 숫자
t = input("정수를 입력하시오: ")
x = int(t)
t = input("정수를 입력하시오: ")
y = int(t)
print(x + y)

# 숫자 -> 문자열
print("나는 현재 " + str(22) + "살이다.")

# 문자열 반복
print("=" * 50)

# 문자열에 변수값 포함
price = 10000
print("상품의 가격은 %s원입니다." % price)

# 개별 문자 추출
s = "Hello Python"
print(s[0])
print(s[1])
print(s[-1])
print(s[6:10])
print(s[-6:-2])
print(s[0:10:2])
print(s[-1:-7:-1])

# 특수 문자열
print("말 한마디로\n천 냥 빚을 갚는다")

# Lab: 친근하게 대화하는 프로그램
print("안녕하세요?")
name = input("이름이 어떻게 되시나요? ")
print("만나서 반갑습니다. " + name)
print("이름의 길이는 다음과 같군요: {}".format(len(name)))
age = int(input("나이가 어떻게 되시나요? "))
print("내년이면 {}이 되시는 군요.".format(age + 1))

# Lab: 연, 월, 일을 합하여 출력하기
year = int(input("오늘의 연도를 입력하시오: "))
month = int(input("오늘의 월을 입력하시오: "))
day = int(input("오늘의 일을 입력하시오: "))
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

# 도전문제
print("오늘은 {}월 {}일 {}년입니다.".format(month, day, year))

# Lab: 2050년에는 몇 살이 될까?
import time

now = time.time()
thisYear = int(1970 + now // (365 * 24 * 3600))
print("올해는 {}입니다.".format(thisYear))

age = int(input("몇 살이신가요? "))
print("2050년에는 {}살이시군요.".format((2050 - thisYear) + age))

# Lab: 소금물의 농도
print("소금물의 농도를 구하는 프로그램입니다.")
salt = int(input("소금의 양은 몇 g입니까? "))
water = int(input("물의 양은 몇 g입니까? "))
concen = salt / (salt + water) * 100
print("소금물의 농도: {:.2f}%".format(concen))

# 리스트에 항목을 동적으로 추가
list = []
list.append(1)
list.append(2)
list.append(6)
list.append(3)

print(list)

# 리스트 요소 접근하기
slist = ['영어', '수학', '사회', '과학']
print(slist[0])
print(len(slist))

# 리스트의 반복
print(slist * 2)

# Lab: 친구들의 리스트 생성하기
friendList = []
friend1 = input("친구의 이름을 입력하시오: ")
friend2 = input("친구의 이름을 입력하시오: ")
friend3 = input("친구의 이름을 입력하시오: ")
friend4 = input("친구의 이름을 입력하시오: ")
friend5 = input("친구의 이름을 입력하시오: ")

friendList = [friend1, friend2, friend3, friend4, friend5]
print(friendList)