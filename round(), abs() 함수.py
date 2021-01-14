#round(a) =>소수 첫째 자리에서 반올림

#R, Python은 5라면 가까운 짝수쪽으로 반올림

print(round(0.5)) #0
print(round(1.5)) #2
print(round(2.5)) #2
print(round(3.5)) #4
print(round(4.5)) #4
print(round(5.5)) #6
print(round(6.5)) #6

#부동소수점 오차에 의해서 round(2.5)가 아닌 round(2.50000~1)이 들어감


print(round(-3.5)) #-4

print(round(6.499999999999999)) #6
print(round(6.500000000000001)) #7

print(round(2.55555, 1)) #2.6 , 첫째자리까지 표시
print(round(2.250, 1)) #2.2 

#파이썬 알고리즘-대표값 문제

#round_half_up이 아닌 round_half_even 방식을 택한다.
a=4.500
print(round(a)) #4, 딱 중앙이면 짝수쪽으로 근사한다.

b=5.500
print(round(b)) #6

a=66.5
a=a+0.5
a=int(a)
print(a) #67

#abs(a) =>절댓값 함수
print(abs(3.5)) #3.5
print(abs(-3.5)) #3.5
