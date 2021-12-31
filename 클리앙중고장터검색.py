# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식을 사용 
import re 

#우리 웹사이트는 웻로봇(웻봇)을 금지~~ 
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#웹사이트에서 페이징처리(0, 1... )
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지면 디코딩 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <span class="subject_fixed" data-role="list-title-text">
	#       맥북프로 2021, 16인치, Pro, 32, 512
	# </span>
        # <span>태그에서 data-role속성이 이렇게 된 것만 필터링 
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                try:
                        title = item.text 
                        if (re.search('애플', title)):
                                print(title.strip())
                except:
                        pass
        
