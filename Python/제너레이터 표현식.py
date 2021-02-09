#제너레이터 표현식

#리스트 표현식은 전체 리스트가 한번에 메모리에 저장 되어야하는 단점
#입력이 적을 때는 괜찮지만 클 때는 메모리를 많이 소모해서 프로그램을 망가뜨리는 원인이 되기도 한다.
    
#파이썬은 이 문제를 해결하려고 리스트 표현식과 제너레이터를 일반화한 제너레이터 표현식을 제공한다.
    
#제너레이터 표현식은 전체 리스트를 한번에 메모리에 로드하지 않고
#대신에 제너레이터 객체를 생성해서 한번에 하나의 리스트 요소만 로드

#리스트 표현식(list comprehension)
arrList= [n for n in range(1, 6)]

print(arrList) #[1, 2, 3, 4, 5]

#제너레이터 표현식 예시1
arrList = (n for n in range(1,6))

for n in arrList:
    print(n)

#제너레이터 표현식 예시2

arrColor = ['black', 'white']
arrSize = ['s', 'm', 'l']
arrDress = ((c, s) for c in arrColor for s in arrSize)
for d in arrDress:
    print(d)

#('black', 's')
#('black', 'm')
#('black', 'l')
#('white', 's')
#('white', 'm')
#('white', 'l')
    
#제너레이터 표현식 예시3
numbers=(1, 2, 3, 4, 5)
squares_under_10 =(number*number for number in numbers if number*number <10)
print(squares_under_10)

#봉우리
#a[i][j] > a[i + dx[k]][j+dy[k]] for k in range(4):
