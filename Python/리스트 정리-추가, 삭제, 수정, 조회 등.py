########################################값 추가하기
#1. append이용 -맨 뒤에 추가됨 
kospi=['삼성전자', 'sk', '카카오', '네이버', 'lg']
kospi.append('tesla')

print(kospi) #['삼성전자', 'sk', '카카오', '네이버', 'lg', 'tesla']


#2. insert이용
kospi=['삼성전자', 'sk', '카카오', '네이버', 'lg']
kospi.insert(2, '농협') #2번 인덱스에 값 추가

print(kospi) #['삼성전자', 'sk', '농협', '카카오', '네이버', 'lg']

#3. +연산자로 더하기
m=[2, 4, 6]
n=[1, 3, 5]
k=m+n
print(k) #[2, 4, 6, 1, 3, 5]

#4. extend이용
m.extend([1, 3, 6])

print(m) #[2, 4, 6, 1, 3, 6]

########################################값 수정하기
kospi=['삼성전자', 'sk', '카카오', '네이버', 'lg']
kospi[4]='tesla'

print(kospi) #['삼성전자', 'sk', '카카오', '네이버', 'tesla']

########################################값 제거하기
#1. del이용 - 값이 반환되지않음
kospi=['삼성전자', 'sk', '카카오', '네이버', 'lg']
del kospi[2] #인덱스가 2인 값을 제거

print(kospi) #['삼성전자', 'sk', '네이버', 'lg']

del kospi[kospi.index('네이버')] #del+index를 이용해서 remove효과도 가능

#2. remove이용 - 값이 반환되지않음, 찾을 값이 없으면 ValueError 발생
kospi=['삼성전자', 'sk', '카카오', '네이버', 'lg']
kospi.remove('네이버') #'네이버'라는 값을 제거


print(kospi) #['삼성전자', 'sk', '카카오', 'lg']

#3. pop 이용 - 값이 반환됨
kospi=['삼성전자', 'sk', '카카오', '네이버', 'lg']
kospi.pop(2) #인덱스가 2인 값을 제거

print(kospi.pop(2)) #pop된 값이 반환된다 #카카오

print(kospi) #['삼성전자', 'sk', '네이버', 'lg']

kospi.pop() #맨 마지막 요소를 제거

########################################값 찾기

#index 함수 - 리스트, 문자열에서 원하는 값의 위치 찾기
#값의 위치를 찾아주는 함수리며, 중복된 값이 있으면 가장 최소의 위치를 리턴

a=[11, 10, 12, 13, 20, 31, 11, 10, 10, 11]

print(a.index(10)) #1출력

print(a.index(10, 2, 9)) #2번째~9번째 위치에서 10의 위치 찾기 #7출력

########################################리스트 슬라이싱

numbers=[0, 1, 2, 4, 5]

numbers[1:3]

########################################리스트 정렬

data=[153, 42, 32, 4, 15]

data.sort()

########################################리스트 정확히 거꾸로 뒤집기

#방법1
data.reverse() #[153, 42, 32, 15, 4]

#방법2
data[::-1] #[153, 42, 32, 15, 4]

print(data)

########################################리스트 요소 세기

data=[1, 2, 2, 3, 4, 3, 'a', 'b', 'b']

data.count(2) #2

data.count('b') #2






