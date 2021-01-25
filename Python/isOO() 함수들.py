#isOO() 함수들
#문자열 체크하기

isalnum #알파벳(한글)과 숫자로만 구성되면 True

isalpha #알파벳(한글)으로만 구성되면 True 아니면 False #숫자 포함 x

isascii #모든 문자가 ASCII 문자이면 True 아니면 False

#정수 판단의 범위 isnumeric()>isdigit()>isdecimal()

isdecimal #10진수 숫자(0~9)면 True 아니면 False

isdigit #일반문자던 특수문자던 숫자 형태(2의 5승 가능)로 이루어지면 True 아니면 False

isnumeric #숫자와 제곱근 분수 등까지 True, 아니면 false

isupper #대문자면 True, 소문자면 False

islower #소문자면 True, 대문자면 False

isprintable #비어있거나 모든 문자열이 프린트 가능하면 True, 아니면 False

isspace #모든 문자가 공백 문자 ' ' 이면 True, 아니면 False

istitle #title 형식에 맞으면 True, 아니면 False

#영문 대문자 앞에는 대문자/소문자가 아닌 문자만 와야 하고
#(대문자 앞에 공백문자가 오는 것이 일반적이지만, 한글 문자 등
#알파벳이 아닌 문자가 있는 경우에도 True를 반환한다.)
#영문 소문자 앞에는 꼭 영문 소문자 또는 대문자가 있어야 한다.


isidentifier #식별자로 사용 될 수 있으면 True, 아니면 False
