"""
selenium == 4.0
pip install --upgrade selenium==4.0
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


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

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY") 
    # execute_script() : 자바스크립트 명령어 실행하는 함수

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
        # END : END키(키보드의 END키와 동일)
    
    # 스크롤 사이 페이지 로딩 시간 추가
    time.sleep(2)
    
    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    
    if after_h == before_h:
        break
    before_h = after_h
    
# 파일 생성
f = open("./Chapter05/data.csv", "w", encoding="cp949", newline="") 
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".basicList_info_area__TWvzp")

for item in items:
    name = item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c").text  
    try: # 예외사항 적용
        price = item.find_element(By.CSS_SELECTOR,".price_num__S2p_v").text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c > a").get_attribute("href")
        # ~ > a : ~ 아래에 있는 a태그
    print(name,price,link)
    
    # (생성한 파일에) 데이터 쓰기
    csvWriter.writerow([name,price,link])
    
# 파일 닫기
f.close()