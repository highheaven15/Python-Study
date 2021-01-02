#sort는 리턴값이 없다.
#sorted는 새로운 리스트를 리턴한다.

#sort는 리스트의 값이 변경된다.
#sorted는 원래 리스트의 값이 변경되지 않는다.

#sorted도 sort처럼 reverse, key parameter 사용 가능 

list=[7,0,2,7,3,6,9]
print(list.sort()) #None, 리턴값이 없다.

list4=list.sort()
print(list4) #None, 이렇게 해도 리턴값이 없다;;

list.sort()
print(list) #[0, 2, 3, 6, 7, 7, 9], 리스트의 값이 변경된다.

list2=[7,0,2,7,3,6,9]

print(sorted(list2)) #[0, 2, 3, 6, 7, 7, 9], 새로운 리스트를 리턴한다.

list3=sorted(list2)
print(list3) #[0, 2, 3, 6, 7, 7, 9]

print(list2) #[7, 0, 2, 7, 3, 6, 9], 원래 리스트의 값이 변경되지 않는다.

#아래 문장 sort함수는 어떤지 모르겠다
#sorted 함수는 시퀸스 자료형 뿐아니라 순서에 구애받지 않는 자료형에도 사용할 수 있다.
#sorted 함수는 문자열 뿐 아니라 튜플, 셋, 딕션어리에서도 가능하며 dict에서는 key값으로 정렬을 한다.
#dict에서 정렬을 할 때 value값을 기준으로 하는 방법은 파라미터로 key를 이용하면 된다.

#sort함수

'''
string = 'hello'
string.sort()
print(string)
'''

#AttributeError: 'str' object has no attribute 'sort'

#sorted함수
string2 = 'hello'
print(sorted(string2)) #['e', 'h', 'l', 'l', 'o']


#거꾸로 정렬-3가지방법

#sort함수

list=[4,5,6]
list.sort(reverse=True)
print(list) #[6, 5, 4]

#sorted함수

list=[7,8,9]
list2=sorted(list, reverse=True)
print(list2) #[9, 8, 7]

#reverse함수

list=[1,2,3]
list.reverse()
print(list) #[3, 2, 1]

strlist=['blue', 'yellow', 'red', 'green', 'Black','Orange']

#대소문자 섞이면 대문자 정렬 후에 소문자 정렬

strlist.sort()
print(strlist) #['Black', 'Orange', 'blue', 'green', 'red', 'yellow']

#대소문 구분없이 정렬(key=str.lower)

strlist.sort(key=str.lower)
print(strlist) #['Black', 'blue', 'green', 'Orange', 'red', 'yellow']



print(sorted("This is a test string from Andrew".split()))

#['Andrew', 'This', 'a', 'from', 'is', 'string', 'test']


print(sorted("This is a test string from Andrew".split(), key=str.lower))

#['a', 'Andrew', 'from', 'is', 'string', 'test', 'This'] , 대소문 구분없이 정렬

#또한 이 key를 사용하는 기술은 정확히 한번만 호출되기 때문에 빠르다는 장점이 있다.


#일반적인 패턴은 객체의 인덱스 중 일부를 키로 사용하여 복잡한 객체를 정렬할 수 있다.

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2])) #숫자에 대해 정렬하겠다.

#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


#https://security-nanglam.tistory.com/376?category=811649
#https://security-nanglam.tistory.com/377
