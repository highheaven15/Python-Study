#딕셔너리의 Counter 모듈

#collections 모듈의 Counter 클래스는 어떤 문자열이나 숫자 리스트가 주어졌을 때, 
#해당 문자열/리스트에서 어떤 객체가 몇번 등장했는지 알아서 카운트, 딕셔너리로 만들어준다.
#이 때 대/소문자가 구별되며, key 값에는 해당 객체가, value 값에는 해당 객체의 등장 횟수가 들어간다.

from collections import Counter

print(Counter('Hello World'))

#Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
