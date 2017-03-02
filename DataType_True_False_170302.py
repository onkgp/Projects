# pylint: disable=C0103
# pylint: disable=C0301

'''자료형의 참과 거짓을 구분하는 기준은 다음과 같다.
    "python"    참
    ""          거짓
    [1, 2, 3]   참
    []          거짓
    ()          거짓
    {}          거짓
    1           참
    0           거짓
    None        거짓'''

# a가 참인 경우에 a.pop()을 계속 실행하라는 의미. 1출력 이후에는 a가 빈 리스트가 되어 거짓이 되므로 실행을 멈춘다.
a = [1, 2, 3, 4]
while a:
    print(a.pop())

# 만약 [1, 2, 3]이 참이면 "True"라는 문자열을 출력하고 그렇지 않으면 "False"라는 문자열을 출력하라.
if [1, 2, 3]:
    print("True")
else:
    print("False")

# 리스트[]가 비어있으므로 False가 출력된다.
if []:
    print("True")
else:
    print("False")
