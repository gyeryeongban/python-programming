# 실습문제 1: 홀수만 누적 덧셈
num = int(input("1부터 어느 수까지의 홀수만 더하시겠습니까? "))
sum = 0

for i in range(1, num+1, 2):
    sum += i
print("1에서 {}까지 홀수의 합: {}".format(num, sum))

# 실습문제 2: 장군 이름 출력하기
nameList = []
nameNum = int(input("몇 명의 장군을 입력하시겠습니까? "))

for i in range(1, nameNum+1):
    name = input("장군의 이름을 입력하세요: ")
    nameList.append(name)

index = 1
for i in nameList:
    print("{}: {} 장군님 반갑습니다!".format(index, i))
    index += 1

# 실습문제 3: 구구단 출력하기
for i in range(2, 10):
    print(i, "단")
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))
    print("")

# 실습문제 4: 다이아몬드 출력하기
num = int(input("다이아몬드의 크기(홀수): "))

for i in range(1, num+1, 2):
    print(" " * ((num - i) // 2) + "*" * i)

for i in range(num-2, 0, -2):
    print(" " * ((num - i) // 2) + "*" * i)

# 실습문제 5: 팩토리얼 계산
num = int(input("팩토리얼 계산을 원하는 값 입력: "))

fac = 1
i = 1

while num >= i:
    fac *= i
    i += 1

print("{}! = {}".format(num, fac))

# 실습문제 6: 숫자 알아내기
import random

computer = random.randint(1, 100)
tries = 0

while tries < 10:
    user = int(input("숫자를 입력하시오: "))
    tries += 1

    if computer > user:
        print("입력하신 숫자보다 더 큰 수입니다.")
        
    elif computer < user:
        print("입력하신 숫자보다 더 작은 수입니다.")
    
    else:
        print(tries, "번의 시도만에 정답을 맞추셨습니다.")
        break

if tries > 10:
    print("10번의 기회를 모두 사용하셨습니다. 정답은 {}입니다.".format(computer))

# 실습문제 7: 범인 찾기 게임
import random

score = 0

while True:
    room = random.randint(1, 3)
    num = int(input("방 번호를 입력하시오: "))

    if num == room:
        print("범인 체포")
        score += 100
        break

    elif num > 3:
        print("{}방은 존재하지 않습니다.".format(n))
        score -= 10
    
    else:
        print("{}방에 범인은 없습니다.".format(num))
        score -= 10

print("게임 종료 점수는 {}입니다.".format(score))

# 실습문제 8: 모든 약수 구하기
num = int(input("자연수 입력: "))

for i in range(1, num+1, 1):
    if num % i == 0:
        print(i, end=" ")