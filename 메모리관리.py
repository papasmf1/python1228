# 메모리관리.py 
class MyClass:
    #초기화(생성자)메서드
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #소멸자메서드 
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(5)
#소멸
#del d 

print("전체 코드 실행 종료")

