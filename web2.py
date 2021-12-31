# web2.py 
#웹서버와 통신
import urllib.request
from bs4 import BeautifulSoup

#블럭 주석 처리: ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
#수열함수로 생성해서 URL을 동적으로 생성(5개의 페이지 50개)
#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for i in range(1,6): 
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    #실행된 페이지(문자열을 검색)
    soup = BeautifulSoup(data, "html.parser")                        
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text 
        print(title.strip())
        f.write(title.strip() + "\n")

f.close() 

