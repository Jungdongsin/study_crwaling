import requests
from bs4 import BeautifulSoup
import pyautogui

# input을 활용하여 검색어 입력받기
keyword = pyautogui.prompt("검색어를 입력하세요 >>> ")
pageNum = 1
lastPage = int(pyautogui.prompt("마지막 페이지번호를 입력해 주세요"))

for i in range(1,lastPage*10,10):
    print(f"{pageNum}페이지 입니다.=================================================")
    
    # 크롤링하고자하는 페이지 불러오기
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".news_tit")

    # 리스트는 for문을 사용
    for link in links:
        title = link.text # 태그 안에 텍스트요소를 가져온더
        url = link.attrs["href"] # href의 속성값을 가져온다
        print(title, url)
    pageNum = pageNum + 1