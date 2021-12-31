# DemoStr.py 

#print( dir(str) )

strA = "python is very powerful"

print( len(strA) )
print( strA.capitalize() )
print( strA.count("p") )
print( strA.count("p",7) )

names = ["전우치","이순신","박문수"]
for name in names:
    print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
    print("=" * 40)


