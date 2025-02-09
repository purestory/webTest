from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수 가져오기
ID = os.getenv('ID')
PASSWORD = os.getenv('PASSWORD')

# 환경변수 검증
if not ID or not PASSWORD:
    raise Exception('환경변수 ID와 PASSWORD가 필요합니다.')

def test_ppomppu():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # 로그인 페이지로 이동
            page.goto('https://www.ppomppu.co.kr/zboard/login.php')
            page.wait_for_timeout(3000)
            
            # 로그인
            page.get_by_role('textbox', name='아이디 입력').fill(ID)
            page.get_by_role('textbox', name='비밀번호 입력').fill(PASSWORD)
            page.get_by_role('textbox', name='비밀번호 입력').press('Enter')
            page.wait_for_timeout(3000)
            
            # 40대 포럼으로 이동
            page.goto('https://www.ppomppu.co.kr/zboard/zboard.php?id=morethan40')
            page.wait_for_timeout(3000)
            
            
        finally:
            browser.close()

if __name__ == '__main__':
    test_ppomppu() 