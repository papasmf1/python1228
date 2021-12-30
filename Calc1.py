class Calc1:
    def __init__(self, x, y):
        self.x=x
        self.y=y   
    def add(self):
        result= self.x+self.y
        return result

b = Calc1(4,7)
print(b.add())