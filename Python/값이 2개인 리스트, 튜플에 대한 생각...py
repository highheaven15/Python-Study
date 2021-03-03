#값이 2개인 리스트, 튜플에 대한 생각..

'''
입력값
5
172 67
183 65
180 70
170 72
181 60
'''
n = int(input())

member=[] #()으로 할수가 없다..튜플은 (값1, 값2)이런식으로만 선언가능
for i in range(n):
    h, w =map(int, input().split())
    member.append((h, w))#튜플 삽입

for h, w in member:
    print(h, w)
'''
172 67
183 65
180 70
170 72
181 60
'''

print(len(member)) #5

for i in range(len(member)):
    print(member[i][0])
    print(member[i][1])
'''
172
67
183
65
180
70
170
72
181
60
'''
