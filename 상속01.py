#부모 클래스 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
    def methodA(self):
        print("methodA()")
    def methodB(self):
        print("methodB()")

#자식 클래스(파생형식은 변수가 추가되는 경우가 많다) 
class Student(Person):
    #상속받은 메서드를 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모의 초기화 메서드를 명시적으로 호출(Java, C# - super, base키워드) 
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 재정의(override)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()
s.methodA()
s.methodB()

