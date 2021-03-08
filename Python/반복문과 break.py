#반복문과 break

#중첩 for문에서 break를 하면 안쪽 for문만 탈출됨으로 breaker변수를 이용해서
#중첩 for문을 한번에 탈출한다.
a=[1, 2, 3, 4, 5]
b=[6, 7, 8]

breaker=True
for index, x in enumerate(a):
    for index2, x2 in enumerate(b):
        print('1')
        if x2==7:
            breaker=False
            break #안쪽의 반복문이 중단된다.
    if(breaker==False):
        print('2')
        break #바깥쪽 반복문이 중단된다.
'''
breaker=True
for index, x in enumerate(a):
    for index2, x2 in enumerate(b):
        print(index, x, index2, x2)
        if x2==7:
            breaker=False
            break
    if(breaker==False):
        break

breaker=True
for index, x in enumerate(a):
    for index2, x2 in enumerate(b):
        print(index, x, index2, x2)
        if x2==7:
            breaker=False
            continue
    if(breaker==False):
        continue
'''

