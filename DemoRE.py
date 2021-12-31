# DemoRE.py 
#정규표현식을 사용(특정한 규칙을 발견)
import re 

#search함수와 match함수 비교 
result = re.search("[0-9]*th", "35th")
print(result.group())
result = re.match("[0-9]*th", "35th")
print(result.group())

