#딕셔너리
#mapping type:mapping object 값의 대응관계를 표시하여 임의의 key값으로 value찾기
#파이썬의 mapping type은 dictionary가 유일하고
#순서x, 중복x, 수정o, 삭제o
#순서와 중복을 허용하지 않는것이 특징

#key에는 list, dict과 같이 내용이 바뀔수 있는 object는 사용불가
#value에는 숫자, 문자, 문자열, 리스트, 튜플도 올수있다.
'''
p=dict()
p[word]=p.get(word, 0)+1
p[word]=p.get(word, 0)-1

for key, val in p.items():
    if val==1:
        print(key)
'''
#딕셔너리 선언
dict={} #중괄호
weekdict=dict()

#딕셔너리 추가 dict[key]=value
weekdict['MON']='맑음'
weekdict['TUE']='구름'
weekdict['SUN']='비'
print(weekdict)
print(weekdict['MON'])

#get(key, 없으면 출력할 값)
print(weekdict.get('FRI')) #None출력
print(weekdict.get('FRI', 0)) #0출력
#print(weekdict['FRI']) #오류난다.

#dict.keys()
print(weekdict.keys()) #dict_keys(['MON', 'TUE', 'SUN'])
print(list(weekdict.keys())) #['MON', 'TUE', 'SUN'] 리스트로 형변환

#dict.values()
print(weekdict.values()) #dict_values(['맑음', '구름', '비'])
print(list(weekdict.values())) #['맑음', '구름', '비']

#dict.items()
print(weekdict.items()) #dict_items([('MON', '맑음'), ('TUE', '구름'), ('SUN', '비')])
print(list(weekdict.items())) #[('MON', '맑음'), ('TUE', '구름'), ('SUN', '비')]
#딕셔너리는 리스트와 다르게 문자, 알파벳, 단어도 index값으로 쓰일수있다.
#리스트는 정수(0, 1, 2, 3, 4, -1, -2...)만 index값으로 사용가능
