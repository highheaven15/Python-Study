#collections의 Counter 모듈

#collections 모듈의 Counter 클래스는 어떤 문자열이나 숫자 리스트가 주어졌을 때, 
#해당 문자열/리스트에서 어떤 객체가 몇번 등장했는지 알아서 카운트, 딕셔너리로 만들어준다.
#이 때 대/소문자가 구별되며, key 값에는 해당 객체가, value 값에는 해당 객체의 등장 횟수가 들어간다.

############################문자열의 경우

#1. 딕셔너리를 이용한 카운팅
def countLetters(word):
    counter=dict()
    for letter in word:
        if letter not in counter:
            counter[letter]=0 #초기값이 없으면 key를 추가 value를 0으로 설정
        counter[letter]+=1
    return counter

print(countLetters('hello world'))
#{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

#2. collections모듈의 Counter클래스를 이용한 카운팅
from collections import Counter

print(Counter('hello world'))
#Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

#1. 딕셔너리를 이용한 최대개수 카운팅
from collections import Counter

def find_max(word):
    counter=Counter(word)
    maxcount=-2187000000
    for letter in counter:
        if counter[letter]>maxcount:
            maxcount=counter[letter]
            maxletter=letter
    return maxletter, maxcount

print(find_max('hello world')) #('l', 3)

#2. collections모듈의 Counter클래스를 이용한 최대개수 카운팅
from collections import Counter
print(Counter('hello world').most_common())
#[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
#데이터가 많은 순으로 정렬된 배열을 리턴

#인자로 k를 넘기면 k개만큼 리턴
print(Counter('hello world').most_common(2))
#[('l', 3), ('o', 2)]

#즉 가장 개수가 많은 k개를 리턴


############################리스트의 경우

#1. 딕셔너리를 이용한 카운팅
my_list  = ['Tick', 'Tock', 'Tock'] # 나의 리스트
new_list = ['Tick', 'Tock', 'Song'] # 추가로 나타난 리스트
counter=dict()
for item in my_list:
    counter[item]=counter.get(item, 0)+1
print(counter) #{'Tick': 1, 'Tock': 2}
for item in new_list:
    counter[item]=counter.get(item, 0)+1
print(counter) #{'Tick': 2, 'Tock': 3, 'Song': 1}
#딕셔너리에 입력 완료

#개수가 큰 순으로 정렬
print(sorted(counter.items(), key=lambda x:x[1], reverse=True))
#[('Tock', 3), ('Tick', 2), ('Song', 1)]

print(sorted(counter.items(), key=lambda x:x[1], reverse=True)[:2])
#[('Tock', 3), ('Tick', 2)]



#2. collections모듈의 Counter클래스를 이용
from collections import Counter
counter =Counter(my_list)
print(counter) #Counter({'Tock': 2, 'Tick': 1})

#추가된 리스트를 누적해서 세기 counter.update()
counter.update(new_list)
print(counter) #Counter({'Tock': 3, 'Tick': 2, 'Song': 1})

print(counter.most_common()) #[('Tock', 3), ('Tick', 2), ('Song', 1)]
#값이 큰 순서대로 나열

print(counter.most_common(1)) #[('Tock', 3)]

print(list(counter.keys())) #['Tick', 'Tock', 'Song']
print(list(counter.values())) #[2, 3, 1]
