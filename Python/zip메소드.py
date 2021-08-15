#zip메소드

#옷의 지퍼(zipper)처럼 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장 함수

#zip()은 여러개의 순회 가능한(iterable) 객체를 인자로 받고
#각 객체가 담소 있는 원소를 튜플 형태로 차례로 접근할수있는 반복자(iterator)를 반환

numbers=[1, 2, 3]
letters=['a', 'b', 'c']

for pair in zip(numbers, letters):
    print(pair)

''' 튜플 형태로 반환
(1, 'a')
(2, 'b')
(3, 'c')
'''
#for문으로 일반적으로 구한경우
for i in range(3):
    pair=(numbers[i], letters[i])
    print(pair) #같은 결과 도출

#zip()함수를 활용하면 여러 그룹의 데이터를 루프를 한번만 돌면서 처리
#가변 인자를 받기 때문에 2개 이상의 인자를 넘겨서 병렬 처리 가능
    
for number, upper, lower in zip('12345', 'asdfg', 'qqqqq'):
    print(number, upper, lower)
'''
1 a q
2 s q
3 d q
4 f q
5 g q
'''

#zip함수로 2개의 튜플의 데이터를 엮은후 리스트로 반환
numbers=(1, 2, 3)
letters=('a', 'b', 'c')

pairs=list(zip(numbers, letters))

print(pairs) #[(1, 'a'), (2, 'b'), (3, 'c')]

number2, letter2=zip(*pairs)

print(number2) #(1, 2, 3)
print(letter2) #('a', 'b', 'c')

#사전으로 활용하기
#두개의 리스트나 튜플로부터 쉽게 사전을 만들수있다.
#키를 담고있는리스트, 값을 담고있는리스트를 zip함수를 이용후 dict로 리턴

keys=[1, 2, 3]
values=['a', 'b', 'c']

print(dict(zip(keys, values))) #{1: 'a', 2: 'b', 3: 'c'}

print(dict(zip(['year', 'month', 'date'], [2001, 1, 31])))
#{'year': 2001, 'month': 1, 'date': 31}

#zip함수 주의사항

#zip함수로 넘기는 인자의 길이가 다를때는 주의
#가장 짧은 인자를 기준으로 데이터가 묶이고 나머지는 버려짐

numbers=['1', '2', '3']
letters=['a']

print(list(zip(numbers, letters))) #[('1', 'a')]
