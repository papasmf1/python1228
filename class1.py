# class1.py 
#클래스 정의(새로운 형식을 정의)
class Person:
    #초기화메서드(가장 먼저 실행)
    def __init__(self):
        #내부의 멤버 변수 초기화
        self.name = "default name"
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본)생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"

p1.print()
p2.print() 


