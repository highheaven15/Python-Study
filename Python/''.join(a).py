b=['1', '2', '3', '4']

print(''.join(b)) #'1234' 문자열 형태로 나온다..
print(int(''.join(b))) #1234 정수 형태로 나온다.

b=[1, 2, 3, 4]
print(''.join(b)) #expected str instance, int found 즉 안먹힌다..    
