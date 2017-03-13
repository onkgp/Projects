# pylint: disable=C0103
# pylint: disable=C0301

number = 23
guess = int(input('Enter an interger : ')) 
#Input 함수는 입력한 문자열을 출력하고 사용자의 입력을 기다린다.
#사용자가 값을 입력하고 [Enter]키를 누르면 Input 함수는 입력값을 문자열의 형태로 변환해준다.
#다음으로 Int(클래스)를 이용하여 이것을 정수형으로 변환한 뒤 그 값을 변수 'guess'에 대입한다.
if guess == number: # 콜론(:)은 다음 줄 부터 새로운 블록이 시작된다는 것을 의미한다.
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
#사용자가 입력한 숫자와 변수(23)를 비교하여 두 숫자가 같으면 위에 정의한 메시지를 화면에 출력한다.
elif guess < number:
    print('No, it is a little higher than that')
#사용자가 입력한 숫자가 변수에 비해 작다면 위에 정의한 메시지를 화면에 출력한다.
else:
    print('No, it is a little lower than that')
#If나 Elif 조건에 해당되지 않는 경우 위에 정의한 메시지를 화면에 출력한다.
print('Done')
#If-Elif-Else문의 실행이 끝나면 If문을 담고 있는 블록의 다음 줄부터 실행을 재개한다.
#위 예제의 경우 그 불록은 최상위 블록(프로그램이 실행된 시점의 블록)이 되며, 따라서 그 다음에 실행될 명령은 print('Done)이 된다.
#그 이후는 프로그램의 끝이므로 실행이 종료되게 된다.
