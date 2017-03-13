# pylint: disable=C0103
# pylint: disable=C0301
# pylint: disable=C0321

# 반복해서 문장을 수행해야 할 경우 While문을 사용한다. 그래서 While문을 반복문이라고도 부른다.
'''기본구조
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>

while문은 조건문이 참인 동안에 while문 아래에 속하는 문장들이 반복해서 수행된다.
'''

# Ex) "열 번 찍어 안 넘어 가는 나무 없다"라는 속담을 만들면 다음과 같다.
treeHit = 0
while treeHit < 10: #treeHit가 10보다 작은 동안에 while문 안의 문장들을 계속 수행한다.
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10: #treeHit가 10이 되면 if문 안의 문장을 수행한다.
        print("나무 넘어갑니다.")
        #마지막 조건문은 10 < 10이므로 [거짓]이 되기 때문에 while문을 빠져나간다(종료)


# While문 직접 만들기 (아래 예제는 IDLE에서 진행해야 함)
'''
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter Number : """
number = 0
while number != 4: #number가 4가 아닌 동안 prompt를 출력한다.
    print(prompt)
    number = int(input()) #사용자의 숫자를 입력 받는다.
'''


# While문 강제로 빠져나가기
coffee = 10
money = 300 #Money가 300으로 고정되어 있어 조건문이 0이 아니므로 항상 참이다. 따라서 무한루프를 돌게 된다.
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee: #Coffee가 0이되면 not coffee가 참이 되므로 If 다음 문장을 수행한다.
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break #Break문이 호출되어 While문을 빠져나간다(종료)


# Break문 이용해 자판기 작동 과정 만들기 - While_break_170306.py 파일 확인


# 조건에 맞지 않는 경우 맨 처음으로 돌아가기(Continue)
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue #a를 2로 나누었을 때 나머지가 0이면 참이다(짝수일때 참). continue문은 While문의 맨 처음 조건문으로 돌아가게 하는 명령어다.
    print(a) #따라서, a가 짝수이면 print(a)는 수행되지 않는다.


# 무한 루프 (아래 예제는 IDLE에서 진행해야 함)
'''기본구조
while True:
    <수행할 문장1>
    <수행할 문장2>

While 조건문이 True이므로 항상 참이 된다. 따라서 While문 안에 있는 문장들은 무한하게 수행된다.
'''

'''
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
'''
