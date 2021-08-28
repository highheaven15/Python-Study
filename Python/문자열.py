#문자열 주요 메소드

#파이썬의 문자열은 불변이므로, 메소드는 새로운 문자열을 반환하므로
#새로운 문자열을 저장해줄 새로운 변수가 필요하다.
# ex) answer2=answer.lower()

#1. 첫글자만 대문자로 바꾸고 나머지 글자는 소문자
str.capitalize()

#2. 모두 소문자 or 대문자로 바꾸기
str.lower()
str.upper()

#3. 대문자->소문자, 소문자->대문자
str.swapcase()

#4. 특정 문자 세기
str.count('a')
str.count('a', 5, 10) #start, end지정시 그 범위안에서만 검색

#5. 특정 문자 포함여부 확인

#단순 포함여부
'home' in str #있으면 True # 없으면False

#포함+인덱스구하기(왼쪽부터 탐색)
str.find('b') #문자열 시작시점의 index반환, 없으면 -1반환
str.index('b') #문자열 시작시점의 index반환, 없으면 ValueError

#포함+인덱스구하기(오른쪽부터 탐색)
str.rfind('b')
str.rindex('b')

#6. 특정 문자로 시작하는지, 끝나는지
str.startswith('Apple')

빼고, 바꾸고, 연속일때, 공백으로 바꾸기, 앞에서 삭제

.isalpha() or x.isdigit()

x.replace()

x.strip()
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
