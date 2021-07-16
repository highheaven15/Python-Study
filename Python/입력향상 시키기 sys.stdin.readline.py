import sys
sys.stdin = open("input.txt", "rt")

input=sys.stdin.readline

a=int(input()) #5

b, c = map(int, input().split())
d=input() #여백을 지워줘야한다.
'''
abcd

'''
d.input().strip() 이나 d.input().rstrip()이 필요하다.

print(d)


strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
