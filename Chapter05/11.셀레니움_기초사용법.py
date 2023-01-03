"""
selenium == 4.0
pip install --upgrade selenium==4.0
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 브라우저 생성
browser = webdriver.Chrome(r"C:\DEV\chromedriver.exe")
    # 크롬드라이버 파일 경로

# 웹 사이트 열기
browser.get("https://www.naver.com/")
browser.implicitly_wait(10) #로딩이 끝날 때까지 10초 딜레이 시키기


# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, "a.nav.shop").click()
    # click() : 클릭을 실행하는 명령어
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR,"input._searchInput_search_text_fSuJ6")
search.click() # 위의 클릭과 동일한 방법

# 검색어 입력
search.send_keys("아이폰 14")
search.send_keys(Keys.ENTER)