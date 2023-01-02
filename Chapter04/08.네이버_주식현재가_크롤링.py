import requests
from bs4 import BeautifulSoup
import openpyxl

"""
# 한개의 종목 크롤링
url = "https://finance.naver.com/item/sise.naver?code=005930"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
price = soup.select_one("#_nowVal").text # 현재가의 텍스트만 가져오기
    # id는 #, class는 .
print(price.replace(",","")) # 콤마 제거를 위해 replace함수 사용"""


# 여러개 종목 크롤링
fpath = r"C:\local_repository\study_crwaling\Chapter04\data.xlsx"
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택

# 종목 코드 리스트
codes = [
    "005930", # 삼성전자
    "000660", # SK하이닉스
    "035720"  # 카카오
]

row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal").text # 현재가의 텍스트만 가져오기
        # id는 #, class는 .
    price = price.replace(",","") # 콤마 제거를 위해 replace함수 사용
    ws[f"B{row}"] = int(price)
    row += 1
    
wb.save(fpath)