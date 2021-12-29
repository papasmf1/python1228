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

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #특정 글자가 postlist에도 있고 그 글자가 result에 없으면 추가 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print( intersect("HAM","SPAM") )



 








