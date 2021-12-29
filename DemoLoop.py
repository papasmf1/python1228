# DemoLoop.py 

value = 5 
while value > 0:
    print(value)
    value -= 1 

print("루프 실행")

lst = [100, 3.14, "문자열"]
#디버깅할 때 중단점(Break Point)
for item in lst:
    print(item, type(item))

#구구단 출력
for x in [2,3,4,5,6]:
    print("--{0}단--".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x,y,x*y))

for x in [1,2,3,4,5,6,7,8,9,10]:
    print("*" * x)

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))
