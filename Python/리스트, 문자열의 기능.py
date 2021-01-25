#문자열

#1.인덱싱
  #0123456789
a='0123456789'
print(a[0])
print(a[1])
print(a[3])
print(a[-1])
print(a[-2])

#2.슬라이싱
#[시작 인덱스:끝 인덱스:간격]

print(a[:2])
print(a[:6])
print(a[1:])
print(a[:]) #전부출력
print(a[0:]) #전부출력
print(a[1::2]) #13579
print(a[-7::2]) #3579
print(a[::-1]) #9876543210
print(a[::-2]) #97531

#3.길이 확인
print(len(a))

#4. 하나하나 접근
for i in a:
    print(i, end=' ') #0 1 2 3 4 5 6 7 8 9

#리스트

#1.인덱싱
     #0  1  2  3  4  5  6  7  8  9
   #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1    
list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[0])
print(list[1])
print(list[3])
print(list[-1])
print(list[-2])

#2.슬라이싱

print(list[:2])
print(list[:6])
print(list[1:])
print(list[:]) 
print(list[0:]) 
print(list[1::2])
print(list[-7::2])
print(list[::-1]) 
print(list[::-2]) #[9, 7, 5, 3, 1]

#3.길이 확인
print(len(list))

#4. 하나하나 접근

for x in list:
    print(x, end=' ') #0 1 2 3 4 5 6 7 8 9 



  
