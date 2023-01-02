import requests
from bs4 import BeautifulSoup
import pyautogui

# input을 활용하여 검색어 입력받기
keyword = pyautogui.prompt("검색어를 입력하세요 >>> ")

# 크롤링하고자하는 페이지 불러오기
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
	# query 뒤에 keyword 변수 사용
html = response.text

soup = BeautifulSoup(html, "html.parser")
    # HTML 텍스트를 가져오기 쉽게 Soup로 만들어야함
links = soup.select(".news_tit")
    # CSS선택자 = 가져오고 싶은 태그를 선택하는 것
# print(links) # 결과는 리스트로 출력됨

# 리스트는 for문을 사용
for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져온더
    url = link.attrs["href"] # href의 속성값을 가져온다
    print(title, url)