# 변수 생성
x = 100

# 변수의 사용
x = 100
x = 200
print(x)

# 변수 2개 생성
x = 100
y = 200

# 변수를 이용한 계산
x = 100
y = 200
sum = x + y
print(sum)

# 변수에 문자열 저장
name = "홍길동"
address = "서울시 종로구 1번지"
print(name)
print(address)

# 도전문제
x = 7
y = 6
print(x + y)

x = '7'
y = '6'
print(x + y)

# 이런 것도 가능하다!
score = 10
score = score + 1

# 여러 값을 함께 출력하기
x = 100
y = 200
sum = x + y
print(x, "과", y, "의 합은", sum, "입니다.")

# 변수의 선언
myVar = 100
type(myVar)
myVar = 100.0
type(myVar)

# 사용자로부터 정수 입력받기
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
sum = x + y
print(x, "과", y, "의 합은", sum, "입니다.")

name = input("이름을 입력하시오: ")
print(name, "씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")

# 도전문제
name = input("이름을 입력하시오: ")
print(name, "씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
sum = x + y
print(x, "과", y, "의 합은", sum, "입니다.")

# 서식을 지원하는 print() 함수 사용법
print("안녕하세요?")

print("100")
print("%d" % 100)

print("100+100")
print("%d" % (100+100))

print("%d" % (100))
print("%d %d" % (100, 200))

# 정수(%d) 외에 자주 사용되는 서식
print("%d / %d = %f" % (100, 200, 0.5))
print("%d / %d = %5.1f" % (100, 200, 0.5))

# format() 함수의 이용
print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))

# 서식 출력 연습
print("%d" % 123)
print("%5d"% 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")

# 다양한 이스케이프 문자
print("한행입니다. 또 한행입니다")
print("한행입니다. \n또 한행입니다")

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과1")
print("\\\\\\ 역슬래쉬 세개 출력")
print(r"\n \t \" \\ 를 그대로 출력")

# 2, 10, 16진수
0b10010011

int('10010011', 2)

0x93 ; int('93', 16)

bin(13) ; bin(0x13) ; bin(0xC5F7)

# 연습: 로봇 기자 만들기
place = input("경기장은 어디입니까? ")
winTeam = input("이긴 팀은 어디입니까? ")
loseTeam = input("진 팀은 어디입니까? ")
bestPlayer = input("우수 선수는 누구입니까? ")
score = input("스코어는 몇 대 몇입니까? ")

print(f"오늘 {place}에서 야구 경기가 열렸습니다.")
print(f"{winTeam}과 {loseTeam}은 치열한 공방전을 펼쳤습니다.")
print(f"{bestPlayer}이 맹활약을 하였습니다.")
print(f"결국 {winTeam}이 {loseTeam}를 {score}로 이겼습니다.")