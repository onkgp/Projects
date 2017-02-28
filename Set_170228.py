# pylint: disable=C0103
# pylint: disable=C0301

'''
집합(Set)의 특징
    - 중복을 허용하지 않는다.
    - 순서가 없다.(Unordered)
    
리스트나 튜플은 순서가 있기때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만 
집합 자료형은 순서가 없기때문에 인덱싱으로 값을 얻을 수 없다.
'''

s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

# Set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환 해야한다.
# 중복을 허용하지 않는 Set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용된다.
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)

t1 = tuple(s1)
print(t1)


# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))

# 합집합
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))

# 차집합
print(s1 - s2)
print(s1.difference(s2))
print(s2.difference(s1))

# 값 1개 추가하기(Add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러 개 추가하기(Update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 특정 값 제거하기(Remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
