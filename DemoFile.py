# DemoFile.py 

#서식문자를 지정
#블럭으로 주석처리: ctrl + / 
# print("{0:x}".format(10))
# print("{0:b}".format(10))
# print("{0:c}".format(65))
# print("{0:e}".format(4/3))
# print("{0:f}".format(4/3))
# print("{0:.2f}".format(4/3))
# #화폐출력
# print("{0:,}".format(15000))

#파일에 쓰기(유니코드로 쓰기와 읽기)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()
print( f.closed )

#파일읽기
f = open("c:\\work\\demo.txt", "rt")
print("---read()---")
print( f.read() )
print( f.tell() )
#리셋하는 코드 
f.seek(0)
print("---readlines()---")
result = f.readlines()
print( result )
f.seek(0)
print("---readline()---")
print( f.readline() ) 
print( f.readline() ) 






