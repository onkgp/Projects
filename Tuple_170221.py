# pylint: disable=C0103

''' 리스트와 튜플의 가장 큰 차이점은 리스트의 항목값은 변경이 가능하지만 튜플은 변경할 수 없다는 것이다.
따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다면 리스트가 아닌 튜플을 사용해야 한다.
튜플은 값을 변화시킬 수 없다는 점만 제외하면 리스트와 기능이 같다.'''

# 튜플의 유형
t1_ = ()
t2_ = (1,) #단, 1개의 요소만을 가질때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3 #리스트와 다르게 괄호를 생략해도 된다.
t5 = ('a', 'b', ('ab', 'cd'))

# 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:])

# 더하기
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
print(t1+t2)

# 곱하기
t1 = (1, 'a', 2, 'b')
print(t1 * 3)

