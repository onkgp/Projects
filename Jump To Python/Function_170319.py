# pylint: disable=C0103
# pylint: disable=C0301
'''함수를 사용하는 이유는 무엇일까?
1. 반복되는 부분이 있을 경우 "반복적으로 사용되는 가치 있는 부분"을 한 뭉치로 묶어서
   "어떤 입력값을 주었을 때 어떤 결과값을 돌려준다"라는 식의 함수로 작성하는 것이 현명하다.
2. 자신이 만든 프로그램을 함수화하면 프로그램의 흐름을 일목요연하게 볼 수 있기 때문이다.

[함수의 구조]
def 함수명(입력인수):
    <수행할 문장1>
    <수행할 문장2>
    ...
def는 함수를 만들 때 사용하는 예약어이며, 함수명은 함수를 만드는 사람이 임의로 만들 수 있다.
함수명 뒤 괄호안의 입력 인수는 이 함수에 입력될 값이란 뜻이다.
이렇게 함수를 정의한 다음 if, while, for문 등과 마찬가지로 함수에서 수행할 문장들을 입력한다.
'''

def _sum(first, second): #이 함수의 이름은 sum이며 입력 인수로 2개의 값을 받는다
    return first + second #입력 인수를 더한다(Return은 함수의 값을 돌려주는 명령어)
x = _sum(3, 4)
print(x)


# 입력값과 결과갑에 따른 함수의 형태
'''
함수는 들어온 입력값을 받아 어떤 처리를 하여 적절한 결과값을 출력한다 (입력값 > 함수 > 출력값)
'''

# 일반적인 함수 (입력값과 결과값이 있는 함수)
'''
결과값을 받을 변수 = 함수명(입력인수1, 입력인수2 ...)
'''
def _sum2(first, second):
    result = first + second
    return result
x = _sum2(1, 10)
print(x)

# 입력값이 없는 함수
'''
결과값을 받을 변수 = 함수명()
'''
def _say():
    return 'Hi'
x = _say()
print(x)

# 결과값이 없는 함수
'''
함수명(입력인수1, 입력인수2 ...)
"4, 6의 합은 10입니다."라는 문장을 출력해 주었는데 왜 결과값이 없다는 것인지 의아하게 생각할 것이다.
Print문은 함수의 구성 요소 중 하나인 <수행할 문장>에 해당될 뿐이어서 결과값은 당연히 없다.
결과값은 Return 명령어로만 돌려받을 수 있다.
'''
def _sum3(first, second):
    print("%d, %d의 합은 %d입니다." % (first, second, first + second))
_sum3(4, 6)

'''
결과값이 진짜 없는지 확인하기 위해 아래 예제를 실행해 보자.
돌려받을 값을 x라는 변수에 대입하여 출력해 보면 None(거짓, 자료형)이 출력되는 것을 알 수 있다.
x = _sum3(4, 6)
print(x)
'''

# 입력값도 결과값도 없는 함수
'''
함수명()
'''
def _say2():
    print('Hi')
_say2() #입력 인수를 받는 곳도 없고 Return문도 없으니 이 함수를 사용하는 방법은 단 한가지다.


# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
'''
[함수의 구조]
def 함수명(*입력변수):
    <수행할 문장1>
    <수행할 문장2>
'''
def _sum_many(*args): #임의로 설정한 변수명 args는 입력 인수를 뜻하는 단어인 arguments의 약자이며 관례적으로 자주 사용한다
                      #변수명 앞에 *을 붙이면 입력값들을 전부 모아서 튜플로 만들어 준다.
    sum4 = 0
    for i in args:
        sum4 = sum4 + i
    return sum4
result = _sum_many(1, 2, 3)
print(result)

result = _sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(result)

def _sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = _sum_mul('sum', 1, 2, 3, 4, 5) #sum을 선택할 때는 if문을 적용하고
print(result)
result = _sum_mul('mul', 1, 2, 3, 4, 5) #mul을 선택하면 elif문을 적용한다
print(result)


# 함수의 결과값은 언제나 하나이다
def _sum_and_mul(a, b):
    return a + b, a * b #함수의 결과값은 2개가 아니라 언제나 1개라 오류가 발생하지 않는다
result = _sum_and_mul(3, 4)
print(result)


