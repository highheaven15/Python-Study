#if __name__ == "__main__":
#    코드
#    코드

# 즉, __name__ == __main__은해당 모듈이 import된 경우가 아니라
# 인터프리터에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령입니다.

//excuteThisModule.py
def func():
    print("function working")

if __name__ == "__main__":
    print("직접 실행")
    print(__name__)
else:
    print("import되어 사용됨")
    print(__name__)


#모듈을 실행할 수 있는 방법은
    
#1. 인터프리터에서 직접 실행하거나
python3 executeThisMoudle.py

#2. 다른 모듈에 import해서 실행하거나.
import executeThisMoudle.py
executeThisMoudle.func()

#__name__은 호출해서 사용한 모듈의 이름을 저장하는 변수이고,

#import를 할 경우 모듈의 이름이 저장된다는 것입니다.

#하지만 직접 실행할 경우 __main__이 들어간다는 것이죠.


