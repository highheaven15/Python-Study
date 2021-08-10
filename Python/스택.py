#스택, stack
#파이썬에서는 리스트로 스택을 흉내낸다.

#stack-init
stack=[]

#stack-push
stack=[1, 2, 3]

stack.append(4) #append 이용

#stack-pop

stack=[1, 2, 3]

top = stack.pop() #pop 이용, 값 리턴 가능

#stack-top

stack=[1, 2, 3]

top=stack[-1] #top원소를 확인
