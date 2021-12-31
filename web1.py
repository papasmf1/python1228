# web1.py 
#웹 크롤링을 위한 선언
from bs4 import BeautifulSoup

#파일을 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8")
#검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#<p>몽땅 검색 
#print(soup.find_all("p"))

#첫번째<p>태그 
#print(soup.find("p"))

#<p class="outer-text"> 조건이 있는 경우
#필터링(걸러내기): class는 파이썬의 키워드 
#print(soup.find_all("p", class_="outer-text"))

#id=first
#print(soup.find_all(id="first"))

#실제 내부의 문자열만 리턴 
for tag in soup.find_all("p"):
    #내부의 문자열만 사용할 경우 text속성 
    content = tag.text.strip() 
    content = content.replace("\n", "")
    print(content)


