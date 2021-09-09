1. 대문자, 소문자(upper, lower)

string="Hello"

string.upper()
string.lower()

2. 문자열 바꾸기(replace)

string="my favorite song is snowman by sia"

string.replace("m", "i") #치환
string.replace("m", "") #삭제
string.replace(" ", "") #공백 삭제

3. 문자열 찾기(find, count)

string="my favorite song is snowman by sia"

string.find("is") #처음나오는 인덱스 리턴 17
string.find("maroon") #없으면 -1

string.count("i") #3
string.count("maroon") #0

4. 문자열 슬라이싱

string="my favorite song is snowman by sia"

string[:]
string[5:]
string[:10]
string[0:2]
string[:-2]
string[::2] 2개씩 step
string[::-1] reverse



5. 문자열 분리 및 결합(split, join)
#리턴결과는 리스트
#split(문자열) 문자열을 기준으로 분리

string="1a2a3a4a"
print(string.split("a")) #['1', '2', '3', '4', '']


string = "apple banana kiwi tomato"
string.split() #공백 기준으로 분리

a=["apple", "kiwi", "banana", "tomato"]
# 리스트의 원소는 모두 str 타입이어야 한다. 아닐경우 오류발생

print("".join(a)) #applekiwibananatomato

print(",".join(a)) #apple,kiwi,banana,tomato

#6. 문자열 공백 제거(strip)

string="        hello world     "

string.strip() #hello world
string.rstrip() #        hello world
string.lstrip() #hello world     

string = "aaaaabbbbbbaaaaa"

print(string.strip("a")) #bbbbbb
#해당 문자가 안나올때까지 왼쪽, 오른쪽 모두에서 제거

print(string.lstrip("a")) #bbbbbbaaaaa
#해당 문자가 안나올때까지 왼쪽에서 제거

print(string.rstrip("a")) #aaaaabbbbbb

print(string.strip("ab")) #공백출력
#양쪽에서 a또는 b가 나오지 않을 때까지 제거
#a 또는 b를 제거하기때문에 공백이 출력된다.

chr(97) #'a'
chr(65) #'A'

ord('b') #98
ord('A') #65

















