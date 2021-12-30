#전역 변수 
str = "Not Class Member"

#클래스 정의 
class GString:
    def __init__(self):
        #인스턴스 멤버 변수 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 실수 
        print(self.str)

#인스턴스 생성
g = GString()
#메서드 호출
g.set("First Message")
g.print()
