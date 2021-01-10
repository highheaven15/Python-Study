#리스트 list

#리스트명 = [요소1, 요소2, 요소3...]

#0부터 인덱싱

#리스트에는 어떠한 자료형도 포함가능

#리스트 슬라이싱

a=[1, 2, 3, 4, 5]

a[0:2] #[1, 2]

a[:3] #처음부터 인덱스 2까지.. [1, 2, 3]

a[2:] #인덱스 2부터 마지막까지

#리스트 연산자

#1. 리스트 더하기
a=[1, 2, 3]
b=[4, 5, 6]

a+b #[1, 2, 3, 4, 5, 6]

#2. 리스트 반복하기
a=[1, 2, 3]
print(a*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]


#리스트 수정

a=[1, 2, 3]

a[2]=4

# a=[1, 2, 4]가 됩니다.

#리스트에서 연속된 범위의 값 수정하기

a[1] =['a', 'b', 'c']
print(a)

a=[1, 2, 3]

a[1:2]= ['a', 'b', 'c']
print(a)

#요소 삭제 하기
a[1:3] =[]
print(a)

del a[1] #a[1]을 삭제

print(a)

a=[1, 2, 3]
a.append(4) #리스트의 맨 마지막에 4를 추가

print(a)


a.sort() #리스트를 오름차순으로 정렬

a=['a', 'b', 'c']
a.reverse() #리스트를 역순으로 뒤집어준다. 정렬하는게 아닌 리스트를 그대로 뒤집는다.

print(a) 

a=[1, 2, 3]
a.index(3) #index함수는 리스트에 x라는 값이 있으면 x의 위치값을 리턴한다.
print(a.index(3))

#리스트에 요소 삽입(insert)

#insert(a, b) 리스트의 a번째 위치에 b를 삽입

a=[1, 2, 3]
a.insert(1, 4)
print(a) #[1, 4, 2, 3]

#리스트 요소 제거(remove)

#remove(x)는 리스트에서 첫번째로 나오는 x를 삭제하는 함수이다.

a=[1, 2, 3, 4, 3, 6]

a.remove(3)
print(a) #[1, 2, 4, 3, 6]

#리스트 요소 끄집어 내기(pop)

a=[1, 2, 3, 4, 5]

a.pop() #pop()은 리스트의 맨 마지막요소를 돌려주고 그 요소는 삭제하는 함수

print(a) #[1, 2, 3, 4]

a.pop(3) #pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제하는 함수

print(a) #[1, 2, 3]

#리스트에 포함된 요소 x의 개수 세기(count)

a=[1, 2, 3, 1]
a.count(1) #리스트에 1이 몇개 포함되어있는지 조사하기 
print(a.count(1)) #2

#리스트 확장(extend)
#extend(x)에서 x는 리스트만 올수있으며 원래의 a리스트에 x리스트를 더하게 된다.
a = [1, 2, 3]
a.extend([4, 5])

print(a) #[1, 2, 3, 4, 5]

#리스트에 들어있는 값 조사(in)

a=[1, 2, 3, 4]
print(1 in a) #True

#튜플 자료형-리스트와의 차이
#1. 리스트는 [ ]로 둘러싸고 튜플은 ( )로 둘러싼다
#2. 리스트는 값의 생성, 삭제, 수정이 가능 , 튜플은 값을 바꿀수없다.

#튜플의 모습
t1=()
t2=(1,)
t3=(1, 2, 3)
t4= 1, 2, 3
t5= ('a', 'b', ('ab', 'cd'))

t1=(1, 2, 'a', 'b')
#del t1[0] #삭제불가, TypeError: 'tuple' object doesn't support item deletion

#t1[0]=3 #수정불가, TypeError: 'tuple' object does not support item assignment

#튜플의 인덱싱, 슬라이싱, 더하기, 곱하기는 리스트와 동일하다.

#튜플에 들어있는 값 조사(in)
b=(1,2, 3,4)
print(2 in b) #True

#set-집합 자료형
#특징1 : 중복을 허용하지 않는다.
#특징2 : 순서가 없다.

s1 = set([1, 2, 3])
print(s1) #{1, 2, 3}

s2=set("Hello")
print(s2) #{'o', 'H', 'e', 'l'}

#set은 순서가 없어서 인덱싱이 불가! 리스트나 튜플로 변환하여 인덱싱 접근 가능

s1= set([1, 2, 3])
l1= list(s1)
print(l1) #[1, 2, 3]
print(l1[2]) #3

t1=tuple(s1)
print(t1)
print(t1[1])

#set에 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1) #{1, 2, 3, 4}

#set에 값 여러개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1) #{1, 2, 3, 4, 5, 6}

#특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1) #{1, 3}


#set 자료형을 활용하는 방법-교집합, 차집합, 합집합에서 유용

s1=set([1, 2, 3, 4, 5, 6])
s2=set([4, 5, 6, 7, 8, 9])

print(s1&s2) #{4, 5, 6}, &는 교집합

s1.intersection(s2) #이것도 교집합, 같은 결과 출력
s2.intersection(s1)

print(s1|s2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}, |는 합집합

s1.union(s2) #이것도 합집합, 같은 결과 출력
s2.union(s1)

print(s1-s2) #{1, 2, 3}
print(s2-s1) #{7, 8, 9}

s1.difference(s2) #{1, 2, 3}
s2.difference(s1) #{7, 8, 9}

#dictionary 딕셔너리

#{key1:value1, key2:value2, key3:value3}
#key에는 변하지 않는값, value에는 변하는 값, 변하지않는값 모두 사용 가능

dic = {'name':'pey', 'phone':'01102034020', 'birth':'1112'}

a={1:'igi'} #key에 정수가능
a={'a': [1,2,3]} #value에 리스트도 가능

#딕셔너리 쌍 추가, 삭제하기

a={1:'a'}
a[2] = 'b' #{2:'b'}쌍 추가

print(a)
{2:'b', 1:'a'}

#삭제
del a[1] #key 가 1인 key:value 쌍 삭제

grade={'pey':10, 'juliet':99}
grade['pey'] #10, key가 'pey'인 딕셔너리의 value값 반환

grade.get('pey') #10

#a.get('name') 과 a['name']의 차이는 없는 key를 입력시 a['name']는 key오류를, a.get('name')는 none을 리턴

#리스트, 튜플은 요소값을 얻어낼때 인덱싱, 슬라이싱 이용
#딕셔너리는 key를 통해 value를 얻어내기밖에 없다.

a={1:'a', 2:'b'}

a[1] #인덱스 1를 의미하는것이 아니라 key가 1인것의 value 반환

#딕션어리는 키의 중복을 피해야한다! 그렇지 않으면 어떤 value를 부를지 알수없다.

#key에 리스트는 사용 불가, 튜플은 사용 가능(변하지 않는 값이므로), 딕션어리도 사용 불가

#a={[1, 2]:'hi'}, key에 리스트 사용 불가

#딕셔너리가 가지는 함수들

#1. key리스트 만들기(keys)

dic = {'name':'pey', 'phone':'01102034020', 'birth':'1112'}

dic.keys()
print(dic.keys()) #dict_keys(['name', 'phone', 'birth'])

#2. value리스트 만들기(values)
dic.values()
print(dic.values()) #dict_values(['pey', '01102034020', '1112'])

#3. key, value 쌍 얻기(items)
dic.items()
print(dic.items()) #dict_items([('name', 'pey'), ('phone', '01102034020'), ('birth', '1112')])

#4. key:value 쌍 모두 지우기(clear)
dic.clear()
print(dic) #{}, 빈 딕셔너리

#딕셔너리 안에 찾으려는 key값이 없는 경우 미리 정해놓은 디폴트 값을 대신 가려오려면
#get(x, '디폴드 값'을 사용하자

a.get('foo', 'bar') #a에는 'foo'라는 키가 없으므로 'bar'를 리턴

#5. 해당 key가 딕셔너리 안에 있는지 조사하기(in)

dic = {'name':'pey', 'phone':'01102034020', 'birth':'1112'}

'name' in dic #True
'email' in dic # False



