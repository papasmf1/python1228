# function2.py 
#불변형식
a = 1.2 
print( id(a) )
a = 2.3
print( id(a) )

print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#전역변수와 지역변수
x = 1 
def func(a):
    return x+a 

#함수 호출
print( func(1) ) 

def func2(a):
    x = 2 
    return x+a 

#호출
print( func2(1) )
