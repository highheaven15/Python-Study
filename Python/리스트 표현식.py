#리스트 표현식- 리스트 매핑

#초급

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number*number)

print(squares)
#[1, 4, 9, 16, 25]

#중급
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x : x*x, numbers)

print(list(squares))
#[1, 4, 9, 16, 25]

#map()함수=function과 리스트를 인자로 받아
#리스트의 모든 요소에 function 적용

#고급 -짧고 의미파악 쉽다.

numbers = [1, 2, 3, 4, 5]
squares = [ number* number for number in numbers]

print(squares)
#[1, 4, 9, 16, 25]


#리스트 표현식-리스트 필터링

#초급

numbers = [1, 2, 3, 4, 5]
numbers_under_4 = []

for number in numbers:
    if number < 4 :
        numbers_under_4.append(number)

print(numbers_under_4)
#[1, 2, 3]

#중급

numbers = [1, 2, 3, 4, 5]

numbers_under_4 =filter(lambda x : x<4 , numbers)

print(list(numbers_under_4))
#[1, 2, 3]


#고급

numbers = [1, 2, 3, 4, 5]

numbers_under_4 = [ number for number in numbers if number <4]

print(numbers_under_4)
#[1, 2, 3]

#리스트 표현식- 리스트 매핑과 리스트 필터링

#초급

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    if number <4:
        squares.append(number * number)

print(squares)
#[1, 4, 9]

#중급

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x : x*x , filter(lambda x : x<4 , numbers))

print(list(squares))
#[1, 4, 9]


#고급

numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers if number <4]

print(squares)
#[1, 4, 9]










