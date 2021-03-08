  #0  1  2  3  4  5  6  7  8
 #-9 -8 -7 -6 -5 -4 -3 -2 -1
a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
for i in range(-1, -5, -1):
    print(a[i], end=' ') #9 8 7 6

#역방향 탐색이라 그런지 -5에 -1을 빼주거나 그런건 안한다..(틀림)
#역방향 탐색은 -1을 빼주는게 아니라 더 해준다.. -5+1까지 즉 -4까지이다.

print()

for i in range(1, 5):
    print(a[i], end=' ') #2 3 4 5

#정방향 탐색은 인덱스 1부터 5-1까지 탐색
'''
print()
for i in range(1, 5, -1):
    print(a[i], end=' ') #이렇게 하면 값이 안나온다

print()
for i in range(5, 1, -1):
    print(a[i], end=' ') #6 5 4 3
    
#for i in range(a, b):는 인덱스 a부터 b-1까지다
#for i in range(b, a, -1):은 인덱스 b부터 a+1까지 거꾸로이다.

for i in range(-2,-n-1,-1):
    #4-10 역수열 문제 다른풀이 
