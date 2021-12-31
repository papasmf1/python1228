# DemoRE.py 
#정규표현식을 사용(특정한 규칙을 발견)
import re 

#search함수와 match함수 비교 
result = re.search("[0-9]*th", "35th")
#찾은 결과를 매칭 오브젝트로 받기
print(result)
print(result.group())
result = re.match("[0-9]*th", "35th")
print(result.group())

print("---함정 추가---")
result = re.search("[0-9]*th", "  35th")
print(result.group())
result = re.match("[0-9]*th", "  35th")
#print(result.group())

print("---apple단어---")
print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))

print("---우편번호---")
print(bool(re.search("\d{5}", "우리 동네는 52300")))
print(bool(re.match("\d{5}", "우리 동네는 52300")))

print("---전화번호---")
telChecker = re.compile("(\d{2,3})-(\d{3,4})-(\d{4})")
print(bool(telChecker.match("02-3429-5000")))
print(bool(telChecker.match("02-가3429-5000")))
print(bool(telChecker.match("0211-가3429-5000")))

