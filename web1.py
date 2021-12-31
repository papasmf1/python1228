# web1.py 
#웹 크롤링을 위한 선언
from bs4 import BeautifulSoup

#파일을 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8")
#검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())


