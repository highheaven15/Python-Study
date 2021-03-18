#deque(double-ended queue) 자료구조

#deque의 생성

import sys
from collections import deque

dq=deque('love')

print(dq) #deque(['l', 'o', 'v', 'e'])

#deque의 길이 제한

dq2=deque(maxlen=3) 


for i in range(5):
    dq2.append(i)
    print(dq2)
    
'''
#오른쪽으로 값이 추가되면 왼쪽에서부터 값이 삭제됩니다.
deque([0], maxlen=3)
deque([0, 1], maxlen=3)
deque([0, 1, 2], maxlen=3)
deque([1, 2, 3], maxlen=3)
deque([2, 3, 4], maxlen=3)
'''

#스택을 구현 : append(), pop()

dq.append('m') #오른쪽 끝에 입력

print(dq) #deque(['l', 'o', 'v', 'e', 'm'])

dq.pop() #오른쪽 끝값을 가져오며 삭제

print(dq) #deque(['l', 'o', 'v', 'e'])


#큐를 구현 : appendleft(), pop(), append(), popleft()

dq.appendleft('a') #왼쪽 끝에 입력

print(dq) #deque(['a', 'l', 'o', 'v', 'e'])

dq.popleft() #왼쪽 끝값을 가져오며 삭제

print(dq) #deque(['l', 'o', 'v', 'e'])


#deque 확장하기 : extend(), extendleft()

print(dq) #deque(['l', 'o', 'v', 'e'])

dq.extend('you')

print(dq) #deque(['l', 'o', 'v', 'e', 'y', 'o', 'u'])

dq.extendleft('A')

print(dq) #deque(['A', 'l', 'o', 'v', 'e', 'y', 'o', 'u'])

dq.extendleft('BCD') #왼쪽으로 확장 되는 순서 주의!!먼저 나온것이 안쪽!

print(dq) #deque(['D', 'C', 'B', 'A', 'l', 'o', 'v', 'e', 'y', 'o', 'u'])


#리스트처럼 사용 : insert(), remove()

dq[2]='K'

print(dq) #deque(['D', 'C', 'K', 'A', 'l', 'o', 'v', 'e', 'y', 'o', 'u'])

dq.insert(0, 'M')

print(dq) #deque(['M', 'D', 'C', 'K', 'A', 'l', 'o', 'v', 'e', 'y', 'o', 'u'])

dq.insert(100, 'M') #100번째 항목(없으니 가장 큰쪽에) 'M'추가

print(dq) #deque(['M', 'D', 'C', 'K', 'A', 'l', 'o', 'v', 'e', 'y', 'o', 'u', 'M'])

dq.remove('M') #'M'이 두개 이상이면 앞에 나온것부터 지운다.

print(dq) #deque(['D', 'C', 'K', 'A', 'l', 'o', 'v', 'e', 'y', 'o', 'u', 'M'])

#메소드들

#1. dq.reverse()
dq.reverse() #deque의 내용을 반전시킨다.

print(dq) #deque(['M', 'u', 'o', 'y', 'e', 'v', 'o', 'l', 'A', 'K', 'C', 'D'])

#2. dq.count()
dq = deque([1, 3, 2, 4, 2, 3, 1])
count = dq.count(2) #count(x)는 deque에 포함된 x의 개수를 반환
print(count)

#3. dq.rotate()
#rotate(n=1)은 deque.appendleft(deque.pop())와 동일하고
#rotate(n=-1)은 deque.append(deque.popleft())와 동일
dq=deque([7, 3, 2, 4, 2, 3, 1])

dq.rotate(1) #오른쪽으로 한칸씩 밀어버린다.

print(dq) #deque([1, 7, 3, 2, 4, 2, 3])

dq.rotate(1)

print(dq) #deque([3, 1, 7, 3, 2, 4, 2])

dq.rotate(-1) #왼쪽으로 한칸씩 밀어버린다.

print(dq) #deque([1, 7, 3, 2, 4, 2, 3])

#4. dq.clear() deque의 값들을 모두 삭제합니다. deque의 길이가 0이 됩니다.

dq.clear()

print(dq) #deque([])
