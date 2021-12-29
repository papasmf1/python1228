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

print("---짝수면 출력---")
for i in lst:
    if i % 2 == 1:
        continue
    print("Item:{0}".format(i))

#기존 언어의 for루프 
for i in range(5):
    print(i)

#수열함수
result = list(range(10))
print(result)
years = list(range(2000,2022))
print(years)
result2 = list(range(10,0,-1))
print(result2)

#리스트 컴프리헨션(리스트 함축, 압축)
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print(result)

d = {100:"apple", 200:"banana", 300:"kiwi"}
print([v.upper() for v in d.values()])

lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링---")
#함수를 정의
def getBiggerThan20(i):
    return i>20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)
