#변수의 scope 설정하기

#다른 scope에 있는 변수를 사용할때가 문제이다.

######case1. 더 넓은 범위에 있는 변수 '읽기'는 가능

n=0
def func():
    print(n) #0
func()


def func1():
    n=1
    def func2():
        print(n) #1
    func2()
func1()

#이렇게 변수를 선언한 곳보다 안쪽에 있는 함수에서는 변수 읽기 가능

######case2. 더 넓은 범위에 있는 변수 '변경'은 불가능

n=0
def func():
    n+=1
    print(n) #local variable 'n' referenced before assignment
func()


def func1():
    n=1
    def func2():
        n+=1
        print(n) #local variable 'n' referenced before assignment
    func2()
func1()

#더 넓은 범위에 있는 변수라도 현재 scope밖에서 선언한 변수라면 변경 불가

########global키워드의 사용

n=1
def func1():
    def func2():
        global n
        n+=1
        print(n) #2
    func2()
func1()

#n을 전역변수로 선언해주고 함수 내부에서 편집을 원할때
#'나는 지금 함수 내의 n이 아닌 전역변수 n을 쓸거야'라는 의미로 global n
#이라고 선언해주면 문제없이 사용이 가능하다.

def func1():
    n=1
    def func2():
        global n
        n+=1
        print(n) #name 'n' is not defined
    func2()
func1()

#전역변수로 선언된 n이 없기때문에 오류가 난다
#이런경우에는 global이 아닌 nonlocal 키워드를 사용해야한다.

def func1():
    n=1
    def func2():
        nonlocal n
        n+=1
        print(n) #2
    func2()
func1()

#위와 같이 현재 scope 내의 지역변수가 아니고 전역변수도 아닌 변수 n을
#사용할때는 nonlocal을 써준다.
#'나는 지금 지역변수는 아닌 변수를 사용할거야'라는 의미로
#nonlocal n이라고 설정해주면 문제없이 사용 가능하다.
