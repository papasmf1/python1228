# function3.py 
#정의되지 않은 인자 처리(필수 + 옵션)
# *ar:모든 것이 옵션인 가변 인자
# **user: 필수 + 옵션 
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print( userURIBuilder("naver.com","80", id="kim", password="1234") )
print( userURIBuilder("naver.com","80", id="kim", password="1234",  
    age="30") )

#람다 함수(간결한 함수 정의)
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )

print( (lambda x:x*x)(3) )
print( globals() )
