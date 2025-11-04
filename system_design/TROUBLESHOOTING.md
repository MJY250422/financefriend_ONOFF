# 🔧 문제 해결 가이드

## 🚨 Python 3.14 문제 (현재 상황)

### 증상
```
Python: 3.14.0
ERROR: Failed building wheel for pydantic-core
ERROR: Failed building wheel for psycopg2-binary
```

### 원인
- ❌ Python 3.14는 아직 개발 버전 (2024년 10월 릴리스)
- ❌ 대부분의 패키지가 Python 3.11~3.12까지만 지원
- ❌ 가상환경(venv311)이 Python 3.14를 사용 중

---

## ✅ 해결 방법

### 🎯 방법 1: 가상환경 재생성 (가장 확실)

```bash
recreate_venv.bat
```

이 스크립트가 자동으로:
1. ✅ 기존 venv311 삭제
2. ✅ Python 3.11로 새 가상환경 생성
3. ✅ 필수 패키지 자동 설치

**실행 후 확인:**
```bash
venv311\Scripts\activate
python --version
# 출력: Python 3.11.x 여야 함!
```

---

### 🎯 방법 2: 수동 재생성

#### Step 1: Python 3.11 설치 확인

```bash
# 설치된 Python 버전 확인
py -0
```

**출력 예시:**
```
Installed Pythons found by py Launcher for Windows
 -3.14          C:\Python314\python.exe
 -3.11          C:\Python311\python.exe  ← 이게 있어야 함!
 -3.10          C:\Python310\python.exe
```

#### Step 2: Python 3.11이 없다면 설치

**다운로드:**
- https://www.python.org/downloads/
- **Python 3.11.x** (최신 3.11 버전) 다운로드
- 설치 시 "Add Python to PATH" 체크

#### Step 3: 가상환경 재생성

```bash
# 기존 가상환경 삭제
rmdir /s /q venv311

# Python 3.11로 새 가상환경 생성
py -3.11 -m venv venv311

# 또는 직접 경로 지정
C:\Python311\python.exe -m venv venv311

# 활성화
venv311\Scripts\activate

# 확인
python --version
# 출력: Python 3.11.x
```

#### Step 4: 패키지 설치

```bash
# pip 업그레이드
python -m pip install --upgrade pip

# 최소 패키지 설치
pip install -r requirements_minimal.txt
```

---

### 🎯 방법 3: Python 3.14 사용 (비추천)

Python 3.14를 계속 사용하려면 (권장하지 않음):

```bash
# 기본 패키지만 설치
pip install fastapi uvicorn sqlalchemy python-dotenv requests

# Pydantic은 최신 개발 버전 시도
pip install --pre pydantic
```

**문제점:**
- ⚠️ 많은 패키지가 불안정
- ⚠️ 예상치 못한 에러 발생 가능
- ⚠️ 프로덕션 사용 불가

---

## 🧪 설치 확인

### 빠른 테스트

```bash
quick_test.bat
```

**예상 출력:**
```
Python version: Python 3.11.x
Python location: ...\venv311\Scripts\python.exe
OK: fastapi
OK: sqlalchemy
OK: requests
OK: pydantic
```

---

## 📋 단계별 완전 해결

### 1️⃣ Python 3.11 설치
```bash
# 설치 여부 확인
py -3.11 --version

# 없으면 설치: https://www.python.org/downloads/
```

### 2️⃣ 가상환경 재생성
```bash
recreate_venv.bat
```

### 3️⃣ 테스트
```bash
quick_test.bat
```

### 4️⃣ 백엔드 실행
```bash
venv311\Scripts\activate
python main.py
```

### 5️⃣ 샘플 데이터 생성
```bash
python create_sample_data.py
```

### 6️⃣ Streamlit 실행
```bash
start_streamlit.bat
```

---

## 🔍 기타 문제

### 한글 깨짐 문제

**배치 파일 첫 줄에 추가:**
```batch
chcp 65001 >nul
```

**PowerShell:**
```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

### 포트 충돌

```bash
# 포트 사용 중인 프로세스 확인
netstat -ano | findstr :8000
netstat -ano | findstr :8501

# 프로세스 종료 (PID 확인 후)
taskkill /PID <PID> /F
```

### ModuleNotFoundError

```bash
# 가상환경 확인
where python
# ...\venv311\Scripts\python.exe 여야 함

# 재활성화
deactivate
venv311\Scripts\activate

# 패키지 재설치
pip install -r requirements_minimal.txt
```

---

## 🎯 권장 설정

### .env 파일
```env
# SQLite 사용 (PostgreSQL 불필요)
DATABASE_URL=sqlite:///./financefriend.db

# CORS
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501

# 서버
API_HOST=0.0.0.0
API_PORT=8000
```

### Python 버전
- ✅ **Python 3.11.x** (권장)
- ✅ Python 3.12.x (가능)
- ⚠️ Python 3.14.x (비추천)

### 데이터베이스
- ✅ **SQLite** (기본, 별도 설치 불필요)
- ⚠️ PostgreSQL (psycopg2-binary 필요)

---

## 📞 여전히 문제가 있다면?

### 정보 수집

```bash
# 1. Python 버전
python --version

# 2. Python 위치
where python

# 3. 설치된 패키지
pip list

# 4. 환경 변수
echo %VIRTUAL_ENV%
```

### 완전 초기화

```bash
# 1. 가상환경 삭제
rmdir /s /q venv311

# 2. 캐시 삭제
pip cache purge

# 3. 재시작
recreate_venv.bat
```

---

## ✅ 체크리스트

- [ ] Python 3.11 설치됨
- [ ] 가상환경이 Python 3.11 사용
- [ ] 필수 패키지 설치 완료
- [ ] .env 파일 생성됨
- [ ] 백엔드가 정상 실행됨
- [ ] 샘플 데이터 생성됨
- [ ] Streamlit 앱 실행됨

---

**가장 빠른 해결: `recreate_venv.bat` 실행!** 🚀




