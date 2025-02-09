# 웹 자동화 테스트 프로젝트

이 프로젝트는 Playwright를 사용한 웹 자동화 테스트 프로젝트입니다.

## 시작하기

### 필수 요구사항
- Python 3.11 이상
- pip (Python 패키지 관리자)

### 설치 방법

1. 저장소 클론:
git clone https://github.com/purestory/webTest.git
cd webTest

2. 가상환경 생성 및 활성화:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. 필요한 패키지 설치:
pip install playwright python-dotenv
playwright install chromium

4. 환경 변수 설정:
cp .env.example .env
`.env` 파일을 열어 실제 ID와 PASSWORD를 입력하세요.

### 실행 방법

테스트 실행:
python test_example.py

## 주요 기능

- 웹사이트 자동 로그인
- 특정 페이지 자동 접속

## 기술 스택

- Python
- Playwright
- python-dotenv