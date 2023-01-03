"""
pip install selenium
pip list # 버전확인
pip install --upgrade pip   # pip 업그레이드
pip install --upgrade selenium  # 최신버전으로 업그레이드
pip install webdriver_manager
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
	# 크롬 드라이버 자동 업데이트
	# pip install webdriver_manager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://www.naver.com")