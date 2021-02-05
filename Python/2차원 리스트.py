#2차원 리스트

str = [ [0, 1, 2], [3, 4, 5], [6, 7, 8]]

for i in str:
    print(i)

for i in str:
    for j in i:
        print(j, end = " ")
    print()

#2차원 리스트의 슬라이싱
#list[행번호][슬라이싱할 열 구간]
