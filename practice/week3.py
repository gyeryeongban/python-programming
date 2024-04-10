# 실습문제 1: 구 부피 계산
radius = float(input("반지름을 입력하세요: "))
volume = 4/3 * 3.141592 * radius ** 3
print("구의 부피 = {:.3f}".format(volume))

# 실습문제 2: 3차 함수 계산
x = int(input("x의 값을 입력하세요: "))
function = 2 * x ** 3 + 3 * x ** 2 + 7 * x + 10
print("2*{}^3 + 3*{}^2 + 7*{} + 10 = {}".format(x, x, x, function))

# 실습문제 3: 은행이자 복리 계산
passYear = int(input("예금 경과 년수를 입력하세요: "))
interest = float(input("예금 금리(%)를 입력하세요: "))
princi = int(input("예금 원금을 입력하세요: "))
money = princi * (1 + interest / 100) ** passYear
print("총 받을 금액: {}원".format(money))

# 실습문제 4: 지폐 교환 프로그램
exchange = int(input("지폐로 교환할 돈을 입력하세요: "))

# 1
# mon50000 = exchange / 50000
# exchange = exchange - (50000 * mon50000)

# mon10000 = exchange / 10000
# exchange = exchange - (10000 * mon10000)

# mon5000 = exchange / 5000
# exchange = exchange - (5000 * mon5000)

# mon1000 = exchange / 1000
# exchange = exchange - (1000 * mon1000)

# 2
mon50000 = exchange // 50000
exchange = exchange % 50000

mon10000 = exchange // 10000
exchange = exchange % 10000

mon5000 = exchange // 5000
exchange = exchange % 5000

mon1000 = exchange // 1000
exchange = exchange % 1000

print("5만원 지폐: {}장".format(mon50000))
print("1만원 지폐: {}장".format(mon10000))
print("5천원 지폐: {}장".format(mon5000))
print("1천원 지폐: {}장".format(mon1000))
print("나머지 잔돈: {}원".format(exchange))

# 실습문제 5: 다항식 계산
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
poly1 = 2 * x**3 + 3 * x**2 * y**2 + 7 * x * z**3 - 5 * y
poly2 = (x + y) / (x * z * 2)
print("2 * {}^3 + 3 * {}^2 * {}^2 + 7 * {} * {}^3 - 5 * {} = {:.2f}".format(x, x, y, x, z, y, poly1))
print("({} + {}) / ({} * {} * 2) = {:.2f}".format(x, y, x, z, poly2))

# 실습문제 6: 두 점 사이의 거리 구하기
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
distance = ((x2 -  x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
print("두 점 사이의 거리: {:.2f}".format(distance))

# 실습문제 7: 비트단위 연산(AND, OR, XOR)
x = int(input("x: "))
y = int(input("y: "))
print("x: ", bin(x))
print("y: ", bin(y))

andCal = x & y
orCal = x | y
xorCal = x ^ y
print("&: {} => {}".format(bin(andCal), andCal))
print("|: {} => {}".format(bin(orCal), orCal))
print("^: {} => {}".format(bin(xorCal), xorCal))