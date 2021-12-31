# web2.py 
#웹서버와 통신
import urllib.request
from bs4 import BeautifulSoup

#블럭 주석 처리: ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#실행된 페이지(문자열을 검색)
soup = BeautifulSoup(data, "html.parser")                        
cartoons = soup.find_all("td", class_="title")
print("찾은 갯수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

