# class1.py 
#클래스 정의(새로운 형식을 정의)
class Person:
    #클래스의 멤버변수로 추가:데이터를 공유하는 것이 목적
    num_person = 0 
    #초기화메서드(가장 먼저 실행)
    def __init__(self):
        #내부의 멤버 변수 초기화
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본)생성
p1 = Person()
p2 = Person() 
print("인스턴스의 갯수:{0}".format(Person.num_person))




