# DemoDict.py 

color = {"apple":"red","kiwi":"green"}
print( len(color) )
print( color["apple"] )

for item in color.items():
    print( item )

#터미널만 보기( ctrl + ~ 틸드)
#입력
color["banana"] = "yellow"
print( color )

#삭제
del color["apple"]
print( color )
