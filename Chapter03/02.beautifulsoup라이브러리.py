import requests
from bs4 import Beautifulsoup

# 네이버 시작 페이지 버튼 크롤링 

# naver 서버에 대화를 시
response = requests.get("http://www.naver.com")

# naver에서 html 줌
html = response.text

# html 번역선생님으로 수프를 만듦
soup = Beautifulsoup(html, "html.parser")

# id 값이 NM_set_home_btn인 놈 한개를 찾아냄
word = soup.select_one("#NM_set_home_btn")
	# select : 여러 개 선택
	# select_one : 한 개 선택
	# a태그의 id값을 선택하는 것이 좋음(id값은 유일)
	# ID는 맨 앞에 #을 붙여준다(#: CSS선택자)
#print(word) # html태그를 포함해서 모두 출력

# 텍스트 요소만 출력
print(word.text)