#문자열 메소드 정리

#파이썬을 다루다 보면 가장 많이 하게 되는 작업 중 하나가 문자열을 다듬는 작업일 것이다.

#파이썬의 문자열은 작은따옴표(' ') 또는 큰따옴표(" ") 사이에
#원하는 문자열을 입력해서 생성할수 있고,

#여러 줄로 된 문자열을 한번에 생성하고 싶은 경우
#작은따옴표나 큰따옴표 3개를 시작과 끝 부분에 입력해서 생성할 수 있다.

#파이썬의 문자열은 불변(immutable) 이므로 메서드가 원래의 문자열을 변경하는 경우는 없다.
#메서드는 항상 새로운 문자열을 반환하므로 이 새로운 문자열을 저장해 줄 새로운 변수를 마련해 주어야 한다



###1. str.capitalize()

#문자열의 첫 글자만 대문자로 바꾸고 나머지는 소문자로 된 문자열을 반환한다.
#첫 문자가 영문 알파벳이 아닌경우는 변환되지 않은 원래 문자 그대로이며 나머지 문자들만 소문자로 바뀐다.
quote = 'SIMPLE IS BETTER THAN COMPLEX.'

print(quote.capitalize())
#Simple is better than complex.

quote2 = '1. SIMPLE IS BETTER THAN COMPLEX.'

print(quote2.capitalize())
#1. simple is better than complex.



###2. str.lower()

#문자열에서 영문 알파벳 문자를 모두 소문자로 바꾼 문자열을 반환한다.
#영문 알파벳이 아닌 문자는 무시한다.

quote = 'SIMPLE IS BETTER THAN COMPLEX.'

print(quote.lower())
#simple is better than complex.

quote2 = '안녕하세요 PYTHON'

print(quote2.lower())
#안녕하세요 python



###3. str.upper()

#문자열에서 영문 알파벳 문자를 모두 대문자로 바꾼 문자열을 반환한다.
#영문 알파벳이 아닌 문자는 무시한다.
quote = 'SIMPLE IS BETTER THAN COMPLEX.'
quote2 = '안녕하세요 PYTHON'
print(quote.upper())
#SIMPLE IS BETTER THAN COMPLEX.
print(quote2.upper())
#'안녕하세요 PYTHON'




###4. str.title()

#문자열을 '타이틀 규칙'에 맞게 바꾼 새 문자열을 반환한다.
#영문 알파벳이 아닌 글자 다음에 나오는 첫 알파벳 문자는 대문자로
#알파벳 문자 뒤에 나오는 알파벳 문자는 소문자로 바꾸는것이다.
#보통은 공백 문자 다음에 나오는 알파벳을 바꾸는 목적
#공백문자가 아닌 어포스트로피(') 등의 문자 뒤에 따라오는 문자도
#대문자로 바꾸어 버리기 때문에 그다지 쓸모있는 메서드는 아닌것 같다.

quote = 'SIMPLE IS BETTER THAN COMPLEX.'

print(quote.title())
#Simple Is Better Than Complex.

quote2 = "you're welcome."

print(quote2.title())
#You'Re Welcome.
#R 은 소문자 r 로 남아있어야 하는데 대문자로 바꿔버림. 개선이 필요하다.




###5. str.casefold()

#문자열을 전부 소문자로 된 문자열을 반환한다.
#str.lower()과 유사하나 더욱 엄격하게 적용된다.
#영어가 아닌 다른 언어(라틴어)에서 차이점을 나타냄

quote = 'SIMPLE IS BETTER THAN COMPLEX.'

print(quote.casefold())
#simple is better than complex.



###6. str.swapcase()

#문자열의 영어 대문자는 소문자로, 소문자는 대문자로 바뀐 문자열을 반환
#영문 알파벳이 아닌 문자는 변하지 않는다.

quote = 'Simple Is Better Than Complex.'

print(quote.swapcase())
#sIMPLE iS bETTER tHAN cOMPLEX.

quote2 = 'python3'

print(quote2.swapcase())
#PYTHON3

quote3 = '안녕하세요'

print(quote3.swapcase())
#안녕하세요



###7. str.center(width[, fillchar])

#width에 지정해준 길이만큼의 빈 문자열을 만들고 원래의 문자열을 이 가운데 위치시킨다.
#옵션으로 fillchar 를 지정해 주면 공백 대신 fillchar 로 공간을 채운다.
#width 가 원래 문자열의 길이보다 작게 지정되었다면 원래의 문자열을 그대로 반환한다.

quote = 'Simple Is Better Than Complex.'

print(quote.center(50))
#          Simple Is Better Than Complex.

print(quote.center(50, '-'))
#----------Simple Is Better Than Complex.----------

print(quote.center(10))
#Simple Is Better Than Complex.



###8. str.ljust(width[, fillchar])

#원래의 문자열을 왼쪽 정렬하고 width로 주어진 길이만큼 공백문자로 채운 문자열을 반환한다.
#옵션으로 fillchar 를 지정해 주면 공백 대신 fillchar 로 공간을 채운다.
#width 가 원래 문자열의 길이보다 작게 지정되었다면 원래의 문자열을 그대로 반환한다.

quote = 'python3'

print(quote.ljust(30))
#python3

print(quote.ljust(30, '-'))
#python3-----------------------



###9. str.rjust(width[, fillchar])

#원래의 문자열을 오른쪽 정렬하고 width로 주어진 길이만큼 공백문자로 채운 문자열을 반환한다.
#옵션으로 fillchar 를 지정해 주면 공백 대신 fillchar 로 공간을 채운다.
#width 가 원래 문자열의 길이보다 작게 지정되었다면 원래의 문자열을 그대로 반환한다.

print(quote.rjust(30))
#                       python3

print(quote.rjust(30, '-'))
#-----------------------python3



###10. str.count(sub[,start[,end]])

#특정 문자열(sub)이 원래 문자열 안에서 몇 번이나 등장하는지를 알려준다.
#옵션으로 start, end를 지정할수 있다. 일반적인 문자열 슬라이스 할때처럼 인덱스를 지정해주면 된다.
#start, end 지정시 그 범위안에서만 검색한다.

quote = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
'''

print(quote.count('is'))
#3

print(quote.count('is', 30))
#2

print(quote.count('is', 30, 60))
#1



###11. str.find(sub[,start[, end]])
#문자열에서 sub로 주어진 문자열을 찾는다.
#sub문자열이 있는 경우는 문자열 시작 지점의 index반환
#sub문자열이 없는 경우는 -1 반환

#문자열이 시작되는 위치를 찾고 싶은 것이 아니라
#그냥 문자열 포함여부를 알고싶다면
#find() 대신 in 연산자를 쓰자

quote = 'Simple is better than complex.'

print(quote.find('e'))
#5

print(quote.find('complex'))
#22

print(quote.find('hello'))
-1

#in 연산자 - 문자열이 있으면 True, 없으면 False 리넡

print('complex' in quote)
#True

print('hello' in quote)
#False



###12. str.rfind(sub[, start[, end]])

#왼쪽부터 검색하는 find()와는 반대로
#문자열에서 sub로 주어진 문자열을 '오른쪽부터'찾는다.
#sub문자열이 있는 경우는 문자열 시작 지점의 index반환
#sub문자열이 없는 경우는 -1 반환
     
quote = 'Simple is better than complex.'

print(quote.rfind('than'))
#17

print(quote.rfind('complex'))
#22

print(quote.rfind('hello'))
#-1



###13. str.index(sub[, start[, end]])

#문자열에서 sub로 주어진 문자열을 찾는다.
#sub문자열이 있는 경우는 문자열 시작 지점의 index반환
#sub문자열이 없는 경우는 ValueError 발생
#find()와 같은 기능이지만, sub 문자열이 없는 경우 ValueError 발생

quote = 'Simple is better than complex.'


print(quote.index('e'))
#5

print(quote.index('complex'))
#22

#print(quote.index('hello'))
#ValueError: substring not found



###14. str.rindex(sub[, start[, end]])

#문자열에서 sub로 주어진 문자열을 찾는다.
#sub문자열이 있는 경우는 문자열 시작 지점의 index반환
#sub문자열이 없는 경우는 ValueError 발생
#rfind()와 같은 기능이지만, sub 문자열이 없는 경우 ValueError 발생

quote = 'Simple is better than complex.'

print(quote.rindex('than'))
#17

print(quote.rindex('complex'))
#22

#print(quote.rindex('hello'))
#ValueError: substring not found



###15. str.startswith(prefix[, start[, end]])

#문자열이 prefix로 주어진 문자열로 시작하는지를 검사해서 True나 False반환
#prefix는 하나의 문자열일수도 있고, 튜플로 여러 문자열을 검사하도록 할수도 있다.
#튜플로 검사하는 경우 원소중 하나 일치하면 True가 반환된다.
#옵션으로 start, end 인덱스 설정 가능 , start 인덱스에서 검사 시작, end 인덱스까지만 검사한다.

quote = 'Simple Is Better Than Complex.'

print(quote.startswith('Sim'))
#True

print(quote.startswith('Sim', 3, 5))
#False

print(quote.startswith(('Sim', 'ple')))
#True



###16. str.endswith(suffix[, start[, end]])

#문자열이 suffix로 주어진 문자열로 끝나는지를 검사해서 True나 False반환
#prefix는 하나의 문자열일수도 있고, 튜플로 여러 문자열을 검사하도록 할수도 있다.
#튜플로 검사하는 경우 원소중 하나 일치하면 True가 반환된다.
#옵션으로 start, end 인덱스 설정 가능 , start 인덱스에서 검사 시작, end 인덱스까지만 검사한다.

quote = 'Simple Is Better Than Complex.'

print(quote.endswith('.'))
#True

print(quote.endswith(('.', ',')))
#True

print(quote.endswith(('_', ',')))
#False

print(quote.endswith('.',0 , 30 ))
#True

print(quote.endswith('.',0 , 29 ))
#False



###17. str.isalnum()

#알파벳 True
#한글 True
#숫자는 True
#공백 문자(' ')는 False
#isalpha(), isdecimal(), isdigit(), isnumeric() 중 하나에 포함되면
#isalnum()에 대해서 True이다.

quote = 'Simple is better than complex.'

print(quote.isalnum())
#False

print(' '.isalnum()) #공백문자는 False
#False

quote2 = 'python3'

print(quote2.isalnum())
#True

quote3 = '안녕하세요'

print(quote3.isalnum())
#True



###18. str.isalpha()

#알파벳 True
#한글 True
#숫자는 False
#공백 문자(' ')는 False
#특수문자는 False

quote = 'python'

print(quote.isalpha())
#True

quote2 = 'python3'

print(quote2.isalpha()) #숫자 포함시 False
#False

print(' '.isalpha()) #공백문자는 False
#False

quote3 = '안녕하세요'

print(quote3.isalpha())
#True



###19. str.isascill()

#모든 문자가 ASCII 문자이면 True 아니면 False
#공백 문자(' ')는 True
# 파이썬 3.7신설

quote = 'Simple is better than complex.'

print(quote.isascii())
#True

quote2 = '안녕하세요'

print(quote2.isascii())
#False



num1='12345' #숫자형 문자열
num2=12345 #숫자형

#숫자형 문자열에 isnumeric(), isdigit(), isdecimal()을 적용해야지
#숫자형에 적용하면 오류난다.


#AttributeError: 'int' object has no attribute 'isdigit'
#AttributeError: 'int' object has no attribute 'isdecimal'
#AttributeError: 'int' object has no attribute 'isnumeric'

######정수 판단의 범위 isnumeric()>isdigit()>isdecimal()

a = '123' #정수형 문자
b = '⅕' #분수형 문자
c='123.45' #소수형 문자는 isnumeric(), isdigit(), isdecimal() 모두 False
d = '5²' #제곱근 문자
e = '①⑼' #특수문자
f = '꘦' #유니코드

#음수는 isnumeric(), isdigit(), isdecimal() 모두 False

###20. str.isnumeric()

#숫자로 인식이 가능하면 True, 아니면 false

print(a.isnumeric())#True
print(b.isnumeric())#True
print(c.isnumeric())#False #소수형 문자 불가능
print(d.isnumeric())#True
print(e.isnumeric())#True
print(f.isnumeric())#True



###21. str.isdigit()

#정수형 문자, 제곱근문자, 특수문자, 유니코드 가능

print(a.isdigit())#True
print(b.isdigit())#False #분수형 문자 불가능
print(c.isdigit())#False #소수형 문자 불가능
print(d.isdigit())#True  
print(e.isdigit())#True  
print(f.isdigit())#True



###22. str.isdecimal()

#10진수 숫자(0~9), 유니코드면 True 아니면 False

print(a.isdecimal())#True
print(b.isdecimal())#False #분수형 문자 불가능
print(c.isdecimal())#False #소수형 문자 불가능
print(d.isdecimal())#False #제곱근 문자 불가능
print(e.isdecimal())#False #특수문자 불가능
print(f.isdecimal())#True



###23. str.islower()

#문자열의 영문 문자가 모두 소문자이면 True, 아니면 False를 반환한다.
#알파벳이 아닌 문자는 무시한다.
#알파벳 문자가 하나도 포함되어 있지 않으면 False를 반환한다.

quote = 'Simple is better than complex.'

print(quote.islower())
#False

quote2 = 'simple is better than complex.'

print(quote2.islower())
#True

quote3 = 'python3'

print(quote3.islower())
#True

quote4 = '안녕하세요 python'

print(quote4.islower())
#True

quote5 = '안녕하세요'
print(quote5.islower()) #알파벳 문자가 하나도 포함되어 있지 않으면 False를 반환한다.
#False



###24. str.isupper()

#문자열의 영문 문자가 모두 대문자이면 True, 아니면 False를 반환한다.
#알파벳이 아닌 문자는 무시한다.
#알파벳 문자가 하나도 포함되어 있지 않으면 False를 반환한다.

quote = 'Simple is better than complex.'

print(quote.isupper())
#False

quote2 = 'SIMPLE IS BETTER THAN COMPLEX.'

print(quote2.isupper())
#True

quote3 = 'PYTHON3'

print(quote3.isupper())
#True

quote4 = '안녕하세요 python'

print(quote4.islower())
#True

quote5 = '안녕하세요'

print(quote5.islower()) #알파벳 문자가 하나도 포함되어 있지 않으면 False를 반환한다.
#False


###25. str.isspace()

#모든 문자가 공백 문자 ' ' 이면 True, 아니면 False

quote = '          '

print(quote.isspace())
#True

quote2 = '          ..?'

print(quote2.isspace())
#False

###26. str.istitle()

#title 형식에 맞으면 True, 아니면 False
#영문 대문자 앞에는 대문자/소문자가 아닌 문자만 와야 하고
#(대문자 앞에 공백문자가 오는 것이 일반적이지만, 한글 문자 등
#알파벳이 아닌 문자가 있는 경우에도 True를 반환한다.)
#영문 소문자 앞에는 꼭 영문 소문자 또는 대문자가 있어야 한다.

quote = 'Simple is better than complex.'

print(quote.istitle())
#False

quote2 = 'Simple Is Better Than Complex.'

print(quote2.istitle())
#True

quote3 = 'SIMPLE Is Better Than Complex.'

print(quote3.istitle())
#False

quote4 = '예를들어Simple Is Better Than Complex.'

print(quote4.istitle())
#True



###27. str.isprintable()

#비어있거나 모든 문자열이 프린트 가능하면 True, 아니면 False
#유니코드의 'other', 'separator'가 프린트 불가능 문자로 분류

a=' '

print(a.isprintable())
#True

b='\t'

print(a.isprintable())
#False

c='\n'

print(a.isprintable())
#False



###28. str. isidentifier()

#식별자(변수명, 클래스명)으로 사용 될 수 있으면 True, 아니면 False

a='varname'

print(a.isidentifier())
#True

b='Classname'

print(b.isidentifier())
#True

c='_underbar'

print(c.isidentifier())
#True

d='0_number'

print(d.isidentifier())
#False

e='-_var_name'

print(e.isidentifier())
#False



###29. str.join(iterable)

#반복 가능한 객체(리스트, 튜플 등)을 인자로 주면 객체의 각 원소를 주어진
#string 을 이용해 연결해서 새로운 문자열을 반환해 준다.
#반복 객체의 원소가 문자열 타입이 아닌 경우에는 TypeError가 발생한다.

words = ['simple', 'is', 'better', 'than', 'complex']

print(' '.join(words))
#simple is better than complex

print('-'.join(words))
#simple-is-better-than-complex

numbers = [1,2,3,4,5]

#print(' '.join(numbers))
#TypeError: sequence item 0: expected str instance, int found



###30. str.split(sep=None, maxsplit=-1)

#주어진 문자열을 sep 문자열이 나오는 곳마다 잘라서 잘린 문자열들로 이루어진 리스트를 반환한다.
#sep을 따로 지정하지 않으면 공백 문자가 나오는 곳마다 자른다.
#이 때 공백문자가 연속해서 나오는 것은 무시하고 공백문자를 제거하고 잘려서 남은 문자열들만 리스트의 원소로 집어넣는다.

#sep을 지정해주면 이 문자열을 기준으로 자르는데, 주어진 문자가 연속해서 나오는 경우에 연속된 sep 문자 사이사이에 빈 문자열이 있는것으로 간주해 빈 문자열 (공백 문자가 아니라 empty string) 를 리스트의 원소로 집어넣는다.
#(즉 default 인 공백 문자를 기준으로 split할때와 동작이 다름)

#maxsplit 을 지정해주면 왼쪽부터 정해진 횟수만큼만 자르는 작업을 해서 리스트로 반환한다.

quote = 'Simple Is Better Than Complex.'

print(quote.split())
#['Simple', 'Is', 'Better', 'Than', 'Complex.']

address = 'http://www.google.com/blahblah'

print(address.split('/'))
#['http:', '', 'www.google.com', 'blahblah']
#// 사이에 빈 문자열 ('') 가 있는 것으로 간주

print(address.split('/', maxsplit=2))
#['http:', '', 'www.google.com/blahblah']



###31. str.rsplit(sep=None, maxsplit=-1)

#주어진 문자열을 sep 문자열이 나오는 곳마다 잘라서 잘린 문자열들로 이루어진 리스트를 반환한다.
#sep을 따로 지정하지 않으면 공백 문자가 나오는 곳마다 자른다.
#maxsplit 을 지정해주면 오른쪽부터 정해진 횟수만큼만 자르는 작업을 해서 리스트로 반환한다.
#오른쪽부터 자르는 점만 제외하면, 왼쪽부터 잘라 나가는 split() 와 동작은 동일하다.

quote = 'Simple Is Better Than Complex.'

print(quote.rsplit())
#['Simple', 'Is', 'Better', 'Than', 'Complex.']

print(quote.rsplit(sep='e'))
#['Simpl', ' Is B', 'tt', 'r Than Compl', 'x.']

print(quote.rsplit(maxsplit=3))
#['Simple Is', 'Better', 'Than', 'Complex.']


###32. str.splitlines([keepends])

#문자열 중에 개행 문자를 찾아 이를 기준으로 문자열을 잘라서 리스트로 반환해준다.
#디폴트는 개행 문자는 제거한 리스트를 반환해 주지만, keepends=True 를 주면 개행문자가 포함된 원소들로 이루어진 리스트를 반환해준다.

#자르는 기준이 되는 개행 문자들은 다음과 같다.

'''
\n : Line Feed

\r : Carriage Return

\r\n : Carriage Return + Line Feed

\v or \x0b : Line Tabulation

\f or \x0c : Form Feed

\x1c : File Separator

\x1d : Group Separator

\x1e : Record Separator

\x85 : Next Line (C1 Control Code)

\u2028 : Line Separator

\u2029 : Paragraph Separator
'''

print('ab c\n\nde fg\rkl\r\n'.splitlines())
#['ab c', '', 'de fg', 'kl']

print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))
#['ab c\n', '\n', 'de fg\r', 'kl\r\n']
#개행문자 포함

#split()과 다르게 마지막 문자가 개행 문자\n 인 경우 거기서 리스트가 끝난다. 
#(split() 은 개행문자 뒤에 빈 line 을 원소로 추가해줌)

print("".splitlines())
#[]

print("One line\n".splitlines())
#['One line']

print(''.split('\n'))
#['']

print('Two lines\n'.split('\n'))
#['Two lines', '']



#유용하게 쓰는 경우는 웹에서 텍스트를 크롤링했을때 원하는 텍스트 앞뒤로 빈칸이 있는 경우가 많은데
#이때 strip(), lstrip(), rstrip() 등을 이용해 빈칸이 제거된 깔끔한 문자열을 얻을수 있다.

###33. str.strip([chars])

#문자열의 '좌우'에 있는 공백 문자들을 제거한 문자열을 반환해준다.
#따로 chars 문자열을 지정해주면 해당 문자열의 문자들로 조합할 수 있는 모든 문자열에 대해 왼쪽과 오른쪽에서 제거를 시도한다.

quote = '    python3    '

print(quote.strip())
#'python3'

quote = 'https://www.google.com'

print(quote.strip('htspomc.'))
#'://www.google'



###34. str.lstrip([chars])

#원래 문자열에서 '왼쪽'에 있는 공백 문자를 전부 제거한 문자열을 반환한다.
#문자열을 인수로 전달하면 공백문자 대신 해당 문자열을 제거한다.
#이 때 정확히 해당 문자열을 제거하는것이 아니고, 주어진 문자열을 조합해서 나올 수 있는 모든 문자열에 대해 제거를 시도한다.

quote = '      python3     '
print(quote.lstrip())
#'python3     '

quote = 'Simple Is Better Than Complex.'
print(quote.lstrip('iSm'))
#'ple Is Better Than Complex.'
#이 경우 제거를 위해 iSm, Sim, miS 등의 모든 조합을 다 시도해 본다는 뜻



###35. str.rstrip([chars])

#원래 문자열에서 오른쪽에 있는 공백 문자를 전부 제거한 문자열을 반환한다.
#문자열을 인수로 전달하면 공백문자 대신 해당 문자열을 제거한다.
#이 때 정확히 해당 문자열을 제거하는것이 아니고, 주어진 문자열을 조합해서 나올 수 있는 모든 문자열에 대해 제거를 시도한다.
#오른쪽에서 제거하는 점을 빼면 lstrip() 과 같다.

quote = '      python3     '

print(quote.rstrip())
#'      python3'

quote = 'Simple Is Better Than Complex.'

print(quote.rstrip('.xle'))
#'Simple Is Better Than Comp'
#이 경우 제거를 위해 .xle, .lex, exl., xe.l 등의 모든 조합을 다 시도해 본다는 뜻



###36. str.partition(sep)

#sep 으로 주어진 문자열이 처음 나오는 곳에서 문자열을 3개로 잘라 튜플로 반환해 준다
#(sep 의 앞부분, sep, sep의 뒷부분).
#원래 문자열에 sep 문자열이 없는 경우에는 원래 문자열과 빈 문자열 2개로 된 튜플을 반환한다.

quote = 'Simple Is Better Than Complex.'

print(quote.partition(' '))
#('Simple', ' ', 'Is Better Than Complex.')

print(quote.partition('Better'))
#('Simple Is ', 'Better', ' Than Complex.')

print(quote.partition('Hello'))
#('Simple Is Better Than Complex.', '', '')



###37. str.rpartition(sep)

#sep 으로 주어진 문자열이 처음 나오는 곳에서 문자열을 3개로 잘라 튜플로 반환해 준다
#(sep 의 앞부분, sep, sep의 뒷부분).
#원래 문자열에 sep 문자열이 없는 경우에는 빈 문자열 2개와 원래 문자열로 된 튜플을 반환한다.

quote = 'Simple Is Better Than Complex.'

print(quote.rpartition(' '))
#('Simple Is Better Than', ' ', 'Complex.')

print(quote.rpartition('Better'))
#('Simple Is ', 'Better', ' Than Complex.')

print(quote.rpartition('Hello'))
#('', '', 'Simple Is Better Than Complex.')



###38. str.replace(old, new[, count])

#문자열 안에서 특정 문자열을 전부 찾아 새로운 문자열로 바꿔 준다.
#개인적으로 프로젝트 관련해서 디렉토리 내의 파일 이름을 대량으로 바꾸는 작업을 할 때가 가끔 있는데 이때 유용하게 쓰는 메서드이다.
#옵션으로 count 를 주면 count 에 주어진 횟수만큼만 바꾸고 작업을 멈춘다.

quote = 'Simple Is Better Than Complex.'

print(quote.replace(' ', '-'))
#Simple-Is-Better-Than-Complex.

print(quote.replace(' ', '-', 2))
#Simple-Is-Better Than Complex.



###39. str.zfill(width)

#원래의 문자열 왼쪽에 숫자 '0' 을 채워 width 만큼의 길이를 가진 문자열을 만들어 반환한다.
#width 가 원래 문자열 길이보다 작으면 원래 문자열을 그대로 반환한다.
#특이점은 문자열이 + 또는 - 기호로 시작하는 경우에는 숫자 0 을 맨 왼쪽부터 채우는 것이 아니고
#+ 또는 - 기호가 가장 먼저 나오고 그 다음 0을 채우고, 그 후에 원래 문자열의 나머지 부분이 나온다.

quote = 'python3'

print(quote.zfill(20))
#'0000000000000python3'

quote = '+2020'

print(quote.zfill(20))
#+0000000000000002020



###39. str.format()

print('hello, {}! you look {}'.format('bob', 'good'))
#hello, bob! you look good

print("You look {1}, {0}!".format('Bob', 'good'))
#You look good, Bob!
# {0}은 'Bob'을 가리키고, {1}은 'good'을 가리킵니다.

print("You look {a}, {b}!".format(a='Tom', b='happy'))
#You look Tom, happy!



###40. str.format_map()

#format()과 같은 역할, 다만, 인자 대신 딕셔너리를 사용합니다.

him ={'name' : 'robert', 'feel' : 'good'}

print('hi, {name}! I feel {feel}'.format_map(him))
#hi, robert! I feel good



###41. str.expandtabs(tabsize=8)

#tab ("\t") 사이즈 조절 (기본 8칸)

a='1\t1'

print(a.expandtabs(4))
#1   1

print(a.expandtabs(10))
#1         1



###42. str.encode(encoding="utf-8", error="strict")

#다양한 문자열을 표현하는 방식이 인코딩

a='변경할 문자열'

print(a.encode("UTF-8"))
#b'\xeb\xb3\x80\xea\xb2\xbd\xed\x95\xa0 \xeb\xac\xb8\xec\x9e\x90\xec\x97\xb4'



###43. str.maketrans(intab, outtab)
###44. translate

#intab의 문자를 outtab문자로 바꾼다.
#translate를 이용하여 문자를 바꾼 뒤 결과를 반환합니다

str = "this is string example....wow!!!"

intab = "aeiou"
outtab = "12345"

result=str.maketrans(intab, outtab)

print(str.translate(result))
#th3s 3s str3ng 2x1mpl2....w4w!!!



###45. removeprefix
###46. removesuffix

#접두사 제거 기능, 접미사 제거 기능

str = 'interoduction to biomedical'


print(str.removeprefix('in'))
#teroduction to biomedical


print(str.removesuffix('cal')) 
#interoduction to biomedi
