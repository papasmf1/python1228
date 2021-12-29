# function1.py 
#함수를 정의
def times(a,b):
    return a*b 

#함수를 호출
print( times(3,4) )

#함수를 정의
def setValue(newValue):
    x = newValue
    print("입력된 값:{0}".format(x))

#호출 
result = setValue(5)
print(result)

#함수정의
def swap(x,y):
    return y,x 

#호출 
print( swap(5,6) )

