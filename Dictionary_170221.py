
# pylint: disable=C0103
# pylint: disable=C0301

dic = {'name': 'kgp', 'phone': '01066557744', 'birth': '800618'}#딕셔너리 예시 name이 Key값 kgp가 Value값

a = {1: 'hi'} #Key로 정수값 1, Value로 문자열 hi 할당
print(a)

a = {'a': [1, 2, 3]} #Key로 문자열 a, Value에 리스트 할당
print(a)

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b' #a딕셔너리에 Key값이 2, Value값이 b인 딕셔너리 쌍을 추가
print(a)
a['name'] = 'conan' #a딕셔너리에 Key값이 name, Value값이 conan인 딕셔너리 쌍을 추가
print(a)

# 딕셔너리 요소 삭제
a = {1: 'a', 2: 'b', 3: 'c'}
del a[1] #a딕셔너리의 Key값이 1인 (Key: Value)쌍을 찾아 삭제한다.
print(a)

# 딕셔너리에서 Key 사용해 Value 얻기
# 리스트나 튜플과 다르게 딕셔너리는 인덱싱이나 슬라이싱을 사용할 수 없고 Key값을 통해서만 Value를 얻어낼 수 있다.
grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

a = {1:'a', 2:'b'}
print(a[1]) #여기서 1은 변수의 두 번째 요소를 지칭하는 것이 아니라 Key값 1일 나타낸다.
print(a[2])

a = {'name': 'kgp', 'phone': '01066557744', 'birth': '800618'}
print(a['name'])

# 딕셔너리 만들 때 주의사항
a = {1: 'a', 1: 'b'} #Key는 고유한 값이므로 중복되게 설정하면 그 중 하나만 출력된다. 출력은 순서대로가 아닌 랜덤이다.
print(a[1])

# Key값으로 튜플은 사용 가능하지만 리스트는 불가능하다.
a = {(1, 2): 'hi'} #튜플은 사용 가능
print(a[1, 2])
'''
a = {[1, 2]: 'hi'} #리스트는 사용 불가능하다. 왜냐하면 리스트는 요소값을 변경할 수 있는 유형이기 때문에 딕셔너리의 Key값으로 적당하지 않다.
print(a[1, 2])
'''

# 딕셔너리 관련 함수들
a = {'name': 'kgp', 'phone': '01066557744', 'birth': '800618'}
print(a.keys()) #딕셔너리 a의 Key값들을 모아서 dict_keys라는 객체를 리턴한다.
                #dict_keys 객체는 리스트를 사용하는 것과 차이가 없지만, 리스트 고유 함수인 append, insert, pop, remove, sort 등의 함수를 수행할 수는 없다.
print(list(a.keys())) # dict_key 객체를 리스트로 변환

# Value 리스트 만들기(Values)
print(a.values()) #딕셔너리 a의 Value값들을 모아서 dict_values라는 객체를 리턴한다.
print(list(a.values())) #dict_values 객체는 리스트를 사용하는 것과 차이가 없지만, 리스트 고유 함수인 append, insert, pop, remove, sort 등의 함수를 수행할 수는 없다.

# Key와 Value 쌍 얻기(Items)
print(a.items()) #Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

# Key와 Value 쌍 모두 지우기(Clear)
print(a.clear()) #clear()함수는 딕셔너리 내의 모든 요소를 삭제한다.

# Key로 Value얻기(Get)
a = {'name': 'kgp', 'phone': '01066557744', 'birth': '800618'}
print(a.get('name')) #get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
print(a['name']) #get(x) 함수를 쓰고 안쓰고의 차이는 print(a['nokey'])는 해당 되는 Key값이 없어 오류가 발생하지만 get(x)함수를 쓰면 아래와 같이 None을 리턴한다.
print(a.get('nokey'))  #출력된 None은 "거짓"이라는 뜻이다.
print(a.get('nokey', 'default')) #Key값이 없을 때 미리 지정한 값을 불러오고 싶은 경우에는 get('x', 'b')형식으로 사용하면 된다. b가 미리 지정한 값이다.

# 찾고 싶은 Key가 딕셔너리 안에 있는지 조사하기(In)
a = {'name': 'kgp', 'phone': '01066557744', 'birth': '800618'}
print('name' in a) #찾고 싶은 Key가 딕셔너리 안에 있으면 참(True)을 리턴한다.
print('email' in a) #찾고 싶은 Key가 딕셔너리 안에 없으면 거짓(False)를 리턴한다.
