# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #기본적으로 인스턴스 멤버 변수가 노출
        #클래스 내부에 숨겨달라(이름 변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #객체의 문자열을 리턴 
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#클래스 외부에서는 변경된 이름: _클래스명__변수명
#print(account1._BankAccount__balance)
print(account1)



