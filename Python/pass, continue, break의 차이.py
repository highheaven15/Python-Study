#pass, continue, break의 차이

#pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행합니다.
#continue : 바로 다음 순번의 loop를 수행한다.
#break : 반복문을 멈추고 loop를 탈출한다. 

for i in range(10):
    if i%2==0:
        pass
        print(i)
    else:
        print(i)
print('done')

#즉, 반복문 수행에있어서 전혀 영향을 끼치지 않습니다.

#pass가 사용되는 경우
#1. 조건문에서 넣어줄 조건이 딱히 없는 경우
#2. class 선언할 때, 초기에 넣어줄 값이 없을 때

for i in range(10):
    if i % 2 == 0:
        continue
        print(i)    
    print(i)
print("Done")
#홀수만 출력됨

#for문의 다음 i를 수행하게 된다.

for i in range(10):
    if i % 2 == 0:
        break
        print(i)    
    else:
        print(i)
print("Done")

#break에 의해 for문이 종료되고 print('done')만 실행된다.
