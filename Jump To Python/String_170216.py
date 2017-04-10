# pylint: disable=C0103
# pylint: disable=C0301

# 문자열에 작은따옴표 포함시키기
food = "Python's favorite food is perl"
print(food)
food = 'Python\'s favorite food is perl'
print(food)

# 문자열에 큰따옴표 포함시키기
say = '"Python is very easy." he says.'
print(say)

# 줄을 바꾸기 위한 이스케이프 코드(\n) 사용
multiline = "Life is too short\nYou need python"
print(multiline)

# 줄을 바꾸기 위한 연속된 큰or작은 따옴표 3개 사용
multiline = '''Life is too short
You need python'''
print(multiline)

# 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun!"
print(head+tail)

# 문자열 곱하기
a = "Python"
print(a*2)

# 문자열 곱하기(응용)
print("="*50)
print("My program")
print("="*50)

# 문자열 인덱싱(Indexing)
a = "Life si too short, You need Python"
print(a[0])
print(a[12])
print(a[-1]) #뒤에서부터 첫 번째 문자를 표시할 때도 0부터 세어야 할 것 같은데 그렇지 않다. 0과 -0의 값은 수학적으로 같은 의미이라서 -0도 0을 뜻하기 때문이다.
print(a[-0])

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0]+a[1]+a[2]+a[3]
print(b)
print(a[0:3]) #e가 출력되지 않는 이유는 a[0:3]을 수식으로 나타내면 [ 0 <= a < 3 ]이라는 뜻이기 때문이다.
print(a[0:4])
print(a[8:11])
print(a[19:]) #끝 번호를 생략하면 (입력한)시작 번호부터 그 문자열의 끝까지 출력한다.
print(a[:17]) #시작 번호를 생략하면 문자열의 처음부터 (입력한) 끝 번호까지 출력한다.
print(a[:]) #시작 번호와 끝 번호를 생략하면 문자열 전체를 출력한다.
print(a[19:-7])

# 슬라이싱 응용 1
a = "20170216Clear"
year = a[0:4]
day = a[4:8]
weather = a[8:]
print(year+"년")
print(day)
print(weather)

# 슬라이싱 응용 2
a = "Pithon"
print(a[:1]+"y"+a[2:])

# 문자열 포매팅
print("I eat %d apples." %3)
print("I eat %s apples." %'five') #문자열을 대입할 때는 큰or작은 따옴표를 사용해야 한다.

number = 3
print("I eat %d apples." %number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

print("Error is %d%%." %98) #문자열 포맷 코드인 %d와 %가 같은 문자열 내에 존재하는 경우, %를 나타내려면 반드시 %%를 사용해햐 한다.

# 포맷 코드를 이용한 정렬과 공백
print("%10s" %"hi") # 전체 길이가 10개인 문자열 공간에소 hi를 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 처리
print("%-10sJane." %"hi")

# 포맷 코드로 소수점 표현하기
print("%10.4f" %3.141592) #전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하고 소수점 4번째 자리까지만 출력 (5번째 소수점은 반올림 처리한다.)

# 문자 개수 세기 (Count)
a = "hobby"
print(a.count('b')) #문자열 중 b의 개수를 출력

# 문자 위치 알려주기 (Find)
a = "Python is best choice"
print(a.find('b')) #문자열 중 b가 처음으로 나온 위치를 출력
print(a.find('k')) #찾는 문자나 문자열이 존재하지 않으면 -1을 반환한다.

# 문자 위치 알려주기 (Index)
a = "Life si too short"
print(a.index('t')) #문자열 중 t가 처음으로 나온 위치를 출력
# print(a.index('k')) #찾는 문자나 문자열이 존재하지 않으면 오류가 발생한다.

# 문자열 삽입 (Join)
a = ","
print(a.join('abcd')) #abcd라는 문자열읠 각각의 문자 사이에 변수 a의 값인 ','를 삽입한다.

# 소문자를 대문자로 변환
a = "hi"
print(a.upper()) #upper() 함수는 소문자를 대문자로 변환한다. 이미 대문자라면 아무런 변환도 일어나지 않는다.

# 대문자를 소문자로 변환
a = "HI"
print(a.lower()) #lower() 함수는 대문자를 소문자로 변환한다. 이미 대문자라면 아무런 변화도 일어나지 않는다.

# 왼쪽 공백 지우기(Lstrip)
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기(Rstrip)
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

# 문자열 바꾸기(Replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기(Split)
a = "Life is too short"
print(a.split()) #괄호안에 값을 넣지 않으면 공백을 기준으로 문자열을 나눈다.
a = "a:b:c:d"
print(a.split(':')) #괄호안에 특정한 값(:)이 있을 경우에는 해당값을 구분자로해서 문자열을 나눈다.

# 고급 문자열 모매팅
print("I eat {0} apples".format(3)) #숫자 대입
print("I eat {0} apples".format("five")) #문자 대입

number = 3
print("I eat {0} apples".format(number)) #숫자 값을 가진 변수 대입

number = 3
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day)) #2개 이상의 변수 대입

print("I ate {number} apples. so I was sick for {day} days.".format(number=3, day="three")) #{0},{1}과 같은 인덱스 대신 {name}형태를 사용함

print("I ate {0} apples. so I was sick for {day} days.".format(3, day="three")) #인덱스와 이름(name) 형태를 혼용해서 사용함

print("{0:<10}".format("hi")) #문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞춘다.
print("{0:>10}".format("hi")) #문자열을 오른쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞춘다.
print("{0:^10}".format("hi")) #문자열을 가운데로 정렬하고 문자열의 총 자릿수를 10으로 맞춘다.
print("{0:=^10}".format("hi")) #정렬 시 공백 문자 대신에 지정한 문자 값으로 채워 넣는다.
print("{0:!<10}".format("hi"))

y = 3.141592
print("{0:0.4f}".format(y)) #소수점 4번째 자리까지만 출력 (5번째 소수점은 반올림 처리한다.

print("{{ and }}".format()) #{}특수문자 표현하기
