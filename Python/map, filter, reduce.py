#map, filter, reduce

#프로그래머스 level2.소수찾기
k=[('1', '7'), ('7', '1')]
alnum=[]
#alnum+=list(map(''.join, k)) #map 이용
#alnum+=[(''.join(i)) for i in k] #리스트 표현식
#alnum+=list(map(lambda x : ''.join(x), k)) #map+lambda이용

a=[1, 2, 3, 4, 5]
b=list(map(str, a)) #['1', '2', '3', '4', '5']
print(b)
a=list(map(int, b)) #[1, 2, 3, 4, 5]
print(a)
c=list(map(lambda x: x+1, a)) #[2, 3, 4, 5, 6]
print(c)
d=list(map(lambda x: int(x)+1, a)) #[2, 3, 4, 5, 6]
print(d)
e=[('1', '2'), ('3', '4'), ('5', '6')]
f=list(map(''.join, e))
print(f) #['12', '34', '56']
g=list(map(lambda x : int(''.join(x)), e))
print(g) #[12, 34, 56]

#map(function_to_apply, list_of_inputs)
#map 함수는 Iterator 를 반환. 리스트, 튜플, 셋 가능
#일반적인 경우
items=[1, 2, 3, 4, 5]
squared=[]
for i in items:
    squared.append(i**2)

#map
items=[1, 2, 3, 4, 5]
squared= list(map(lambda x:x**2, items))
print(squared)
squared= tuple(map(lambda x:x**2, items))
print(squared)
squared= set(map(lambda x:x**2, items))
print(squared)

#map->list comprehension
squared=[x**2 for x in items]
print(squared)

#filter
number_list=range(-5, 5)
less_than_zero=list(filter(lambda x : x<0, number_list))
print(less_than_zero)

#filter->list comprehension
less_than_zero=[x for x in number_list if x<0]
print(less_than_zero)

#reduce 잘모르겠음 누적시키는것?
sum_value=reduce((lambda x, y : x+y), [x for x in range(1, 101)])
print(sum_value)


