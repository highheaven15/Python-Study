#리스트 복사

#리스트=리스트 선언시 복사가 아닌 참조가 되어 값을 한리스트에서 변경을
#하면 똑같이 다른리스트가 변경이 된다.

#1. 동일한 크기의리스트를 준비하고 각 원소를 하나씩 복사하는 방법
#2. 슬라이싱을 이용한 복사방법
#3. 리스트 객체의 copy함수

money=[1, 2, 3, 4, 5]

money2=money[:]

print(money2) #[1, 2, 3, 4, 5]

money=[2, 3, 4, 5, 6]

money3=money.copy()

print(money3) #[2, 3, 4, 5, 6]
