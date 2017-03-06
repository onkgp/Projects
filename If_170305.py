# pylint: disable=C0103
# pylint: disable=C0301

money = 1 #1은 참이다.
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# If문의 기본 구조
'''
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장1
    수행할 문장2
    ...
조건문을 테스트해서 참이면 if문 바로 다음의 문자(if블록)들을 수행하고,
조건문이 거짓이면 else문 다음의 문장(else블록)들을 수행하게 된다.
그러므로 else는 if문 없이 독립적으로 사용할 수 없다.
'''
# 들여쓰기
'''
if조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
if문을 만들 때는 if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(Indentation)를 해주어야 한다.

다음과 같이 작성하면 오류가 발생한다
if 조건문:
    수행할 문장1
수행할 문장2
    수행할 문장3

※ 파이썬 커뮤니티에서는 들여쓰기를 할 때 공백(Spacebar) 4개를 사용하는 것을 권장한다.
※ 조건문 다음에 콜론(:)을 잊지 말것!
※ 참고로 다른 언어에서는 if문을 {}기호로 감싸지만 파이썬에서는 들여쓰기를 사용한다.
'''

# 조건문이란 무엇인가?
'''
if 조건문에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다.
자료형의 참과 거짓에 대해서 몇 가지만 살펴보면 다음과 같은 것들이 있다.
                [참]        [거짓]
숫자 :     0이 아닌 숫자       0
문자열 :   "abc"              ""
리스트 :   [1, 2, 3]          []
튜플   :   (1, 2, 3)          ()
딕셔너리 :  {"a": "b"}        {}
'''

# 비교연산자
'''
조건이 참인지 거짓인지 판단할 때 자료형보다는 비교연산자를 쓰는 경우가 훨씬 많다
x < y    : x가 y보다 작다
x > y    : x가 y보다 크다
x == y   : x와 y가 같다
x != y   : x와 y가 같지 않다
x <= y   : x가 y보다 작거나 같다
x >= y   : x가 y보다 크거나 같다
'''
x = 3
y = 2
print(x > y) #x > y라는 조건문이 참이기 때문에 True를 출력한다.
print(x < y) #조건문이 거짓이기 때문에 False를 출력한다.
print(x == y) #x와 y는 같지 않기 때문에 False를 출력한다.
print(x != y) #x와 y는 같지 않기 때문에 True를 출력한다.

# Ex)만약 3,000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라""
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라") #money >= 3000 이라는 조건문이 거짓이 되기 때문에 else문 다음의 문장을 수행한다.


# And, Or, Not
'''
x or y    : x와 y 둘중에 하나만 참이면 참이다
x and y   : x와 y 모두 참이어야 참이다
not x     : x가 거짓이면 참이다
'''
# Ex) 돈이 3,000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# x in s, x not in s
'''
[in]              [not in]
x in 리스트      x not in 리스트
x in 튜플        x not in 튜플
x in 문자열      x not int 문자열
'''
print(1 in [1, 2, 3]) #리스트 안에 1이 있는가? 라는 조건문이다. 1이 있으므로 True를 리턴한다.
print(1 not in [1, 2, 3]) #리스트 안에 1이 없는가? 라는 조건문이다. 1이 있으므로 False를 리턴한다.

print('a' in ('a', 'b', 'c')) #튜플 안에 a가 있으므로 True를 리턴한다.

print('j' not in 'python') #문자열 안에 j가 없으므로 True를 리턴한다.

# Ex) 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# Ex) 주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass #조건을 만족하면 아무런 결과도 출력하지 않는다.
else:
    print("카드를 꺼내라")


# 다양한 조건을 판단하는 elif

# Ex) 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
# 조건을 판단하는 부분이 두 군데(주머니에 돈이 있는지 판단, 없다면 카드가 있는지 판단)있는 예시인데 if와 else로 표현하면 다음과 같다
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

# elif를 사용하면 더 간단하게 작성할 수 있다. elif는 이전 조건문이 거짓을 때 수행된다.
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

# If, Elif, Else문의 기본 구조 (Elif는 개수에 제한 없이 사용할 수 있다)
'''
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
elif:
    수행할 문장1
    수행할 문장2
    ...
elif:
    수행할 문장1
    수행할 문장2
    ...
...
else:
    수행할 문장1
    수행할 문장2
    ...
'''

# If문을 한 줄로 작성하기 (때로는 이렇게 작성하는 것이 보기 편할 수 있다)
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
