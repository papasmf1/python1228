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

#불변형식을 읽기+쓰기(정수, 실수, 복소수, 문자열, 튜플)
g = 1 

def testScope(a):
    #global g 
    g = 2 
    return a+g 

#호출
print( testScope(1) )
print("g:", g)


#기본값 셋팅(옵션인 경우)
def times(a=10,b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자(매개변수명을 기술):URL, URI 
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print( connectURI("naver.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변인자(갯수가 가변적인 경우 Tuple로 받기)
def union(*ar):
    #지역변수 초기화 
    result = []
    #HAM(0) | EGG(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            #아직 없으면 추가 
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )

