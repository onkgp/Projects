# pylint: disable=C0103
# pylint: disable=C0301
# pylint: disable=C0321

'''기본구조
for 변수 in 리스트(또는 튜플, 문자열):
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>

리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 <수행할 문장1> <수행할 문장2> 등이 수행된다
'''

# 전형적인 For문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i) #변수(i)에 리스트의 첫 번째 요소인 'one'을 대입하고 그 다음 'two' 마지막으로 'three'를 대입하고 종료한다.

# 다양한 For문
a = [(1, 2), (3, 4), (5, 6)] #리스트의 요소값이 튜플
for (first, last) in a: #각각의 요소들이 자동으로 first와 last라는 변수에 대입된다.
    print(first + last) #튜플안의 요소를 더한 값을 출력한다.

# For문 응용 (총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오.)
marks = [90, 25, 60, 45, 80] #5명의 시험 점수를 리스트로 표현함. 첫번째 학생은 90점 다섯번째 학생은 80점이다.
number = 0 #각각의 학생에게 번호를 붙여주기 위해 number라는 변수 사용
for mark in marks: #점수 리스트인 marks에서 차례로 점수를 꺼내 mark라는 변수에 대입하고 for문 안의 문장들을 수행한다.
    number = number + 1 #for문이 한 번씩 수행될 때마다 number는 1씩 증가한다.
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number) #점수가 60점 이상이면 합격 메시지를 출력한다.
    else:
        print("%d번 학생은 불합격입니다." % number) #점수가 60점 미만이면  불합격 메시지를 출력한다.

# For문과 Continue (For문 안의 문장을 수행하는 도중에 Continue문을 만나면 For문의 처음으로 돌아가게 된다.)
# 앞의 응용 예제를 그대로 이용해서 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 코드를 작성해 보자.
marks = [90, 25, 60, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue #점수가 60점 이하인 학생일 경우에는 mark < 60이 참이 되어 Continue문이 수행된다.
                           #따라서 축하메시지를 출력하는 부분인 print문을 수행하지 않고 For문의 처음으로 돌아가게 된다.
    print("%d번 학생 축하합니다. 합격입니다." % number)

# For와 함께 자주 사용하는 Range 함수
a = range(10) #range함수를 이용해 0부터 10미만의 숫자를 포함하는 range 객체를 생성
print(a)

a = range(1, 11) #1이 시작 숫자, 11은 끝 숫자인데 이때 끝 숫자는 객체에 포함되지 않는다.
print(a)

# For와 Range 함수를 이용해 1부터 10까지 더하기
sum = 0
for i in range(1, 11): #숫자 1부터 10까지(1이상 11미만)의 숫자를 i변수에 하니씩 차례로 대입한다
    sum = sum + i
print(sum)

# 앞의 응용 예제를 Range 함수를 이용해 작성
marks = [90, 25, 60, 45, 80]
for number in range(len(marks)): #len 함수는 리스트 내 요소의 개수를 반환하는 함수이다. 따라서 len(marks)는 5가되고 최종 적으로 range(5)를 의미한다
    if marks[number] < 60: continue #number 변수에는 차례로 0부터 4까지의 숫자가 대입된다. 즉 marks[0]번째 요소인 90점 부터 대입된다
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# For와 Range 함수를 이용한 구구단 구현
for i in range(2, 10): #2부터 9까지의 숫자가 변수 i에 대입된다.
    for j in range(1, 10): #1부터 9까자의 숫자가 변수 j에 대입된다.
        print(i * j, end=" ") #변수 i와 j를 곱한 결과를 출력한다. end를 넣어준 이유는 해당 결과값을 출력할 때 다음줄로 넘기지 않고 같은 줄에 출력하기 위해서다.
    print('') #2단, 3단 등을 구분하기 위해 for문이 끝나면 결과 값을 다음 줄부터 출력하게 해주는 문장이다.


# 리스트 안에 For문 포함하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result) #a라는 리스트의 각 항목에 3을 곱한 결과를 result라는 리스트에 담아라
# List comprehension를 이용하면 조금더 편리하고 직관적인 코드를 작성할 수 있다
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 짝수에만 3을 곱하기
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0] #결과값 중 2로 나눈 나머지가 0인 것만 출력해라
print(result)

'''List comprehension의 기본 문법
[표현식 for 항목1 in 반복가능객체1 if 조건1]
[표현식 for 항목2 in 반복가능객체2 if 조건2]
...
[표현식 for 항목n in 반복가능객체n if 조건n]
'''

# 구구단의 모든 결과를 리스트에 담아라
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
