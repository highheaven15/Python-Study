#얕은 복사, 깊은 복사

#https://kongdols-room.tistory.com/67
#https://blueshw.github.io/2016/01/20/shallow-copy-deep-copy/#3-%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%ACdeep-copy
#https://crackerjacks.tistory.com/14

#1. 단순 객체 복제
#변수만 복사하다보니 바라보는 객체가 동일, 두 변수중 하나만 변경되어도 나머지도
#동일하게 수정된다.
#2.얕은 복사-가변형(mutable)자료형 변경시 같이 변경됨, 불변형(immutable)자료형은 변경안됨
#3.깊은 복사-가변형, 불변형 모두 변경 안됨

#가변형-리스트, 셋, 딕셔너리
#불변형-str, int, float, bool, 튜플

import copy

a=[1, [1, 2, 3]]
b=a.copy() #얕은 복사

print(b) #[1, [1, 2, 3]]

c=copy.deepcopy(a) #깊은 복사

print(c)

a[1][2]=99 #가변형 자료 변경시..

print(a) #[1, [1, 2, 99]]
print(b) #[1, [1, 2, 99]]
print(c) #[1, [1, 2, 3]]


a[0]=6 #불변형 자료 변경시..

print(a) #[6, [1, 2, 99]]
print(b) #[1, [1, 2, 99]]
print(c) #[1, [1, 2, 3]]









