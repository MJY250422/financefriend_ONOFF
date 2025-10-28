# 🧪 백엔드-Streamlit 통합 테스트 가이드

이 가이드는 백엔드 API와 Streamlit 웹 애플리케이션을 연동하여 테스트하는 방법을 설명합니다.

## 📋 목차

1. [사전 준비](#사전-준비)
2. [환경 설정](#환경-설정)
3. [서버 실행](#서버-실행)
4. [테스트 방법](#테스트-방법)
5. [문제 해결](#문제-해결)

---

## 🔧 사전 준비

### 필수 요구사항

- Python 3.11 이상
- 가상환경 (venv311)
- PostgreSQL 또는 SQLite (개발용)

### 디렉토리 구조

```
financefriend_ONOFF/
├── system_design/          # 백엔드 서버
│   ├── main.py
│   ├── database.py
│   ├── routers/
│   ├── .env               # 환경 설정 (생성 필요)
│   ├── .env.example       # 환경 설정 예시
│   ├── venv311/           # 가상환경
│   ├── run_servers.bat    # Windows 실행 스크립트
│   ├── run_servers.ps1    # PowerShell 실행 스크립트
│   ├── test_integration.py    # API 통합 테스트
│   └── create_sample_data.py  # 샘플 데이터 생성
│
└── streamlit/             # Streamlit 앱
    ├── streamlit_app.py.py
    ├── api_client.py      # 백엔드 API 클라이언트
    ├── test_backend.py    # 백엔드 테스트 페이지
    ├── core/
    ├── ui/
    └── requirements.txt
```

---

## ⚙️ 환경 설정

### 1. 환경 변수 설정

`.env.example` 파일을 `.env`로 복사하고 필요한 설정을 수정합니다.

```bash
# system_design 디렉토리에서 실행
copy .env.example .env
```

**주요 설정 항목:**

```env
# 백엔드 서버 설정
API_HOST=0.0.0.0
API_PORT=8000

# CORS 설정 (Streamlit 허용)
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501

# 데이터베이스 설정 (SQLite 사용)
DATABASE_URL=sqlite:///./financefriend.db

# 또는 PostgreSQL 사용
# DATABASE_URL=postgresql://user:password@localhost:5432/financefriend
```

### 2. 패키지 설치

#### 백엔드 패키지

```bash
cd system_design
venv311\Scripts\activate
pip install -r requirements.txt
```

#### Streamlit 패키지

```bash
cd ..\streamlit
..\system_design\venv311\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 서버 실행

### 방법 1: 자동 실행 스크립트 (권장)

#### Windows 배치 파일

```bash
# system_design 디렉토리에서
run_servers.bat
```

#### PowerShell 스크립트

```powershell
# system_design 디렉토리에서
.\run_servers.ps1
```

이 스크립트는 다음을 자동으로 수행합니다:
- ✅ .env 파일 확인 및 생성
- ✅ 백엔드 서버 실행 (포트 8000)
- ✅ Streamlit 앱 실행 (포트 8501)
- ✅ 브라우저 자동 열기

### 방법 2: 수동 실행

#### 1️⃣ 백엔드 서버 실행

```bash
cd system_design
venv311\Scripts\activate
python main.py
```

백엔드 서버가 실행되면 다음 주소에서 접근할 수 있습니다:
- 🌐 API 서버: http://localhost:8000
- 📚 Swagger UI: http://localhost:8000/docs
- 📖 ReDoc: http://localhost:8000/redoc

#### 2️⃣ Streamlit 앱 실행 (새 터미널)

```bash
cd streamlit
..\system_design\venv311\Scripts\activate
streamlit run app.py
```

Streamlit 앱이 자동으로 브라우저에서 열립니다:
- 🖥️ Streamlit 앱: http://localhost:8501

---

## 🧪 테스트 방법

### 1. API 통합 테스트 (자동)

백엔드 API의 모든 엔드포인트를 자동으로 테스트합니다.

```bash
cd system_design
venv311\Scripts\activate
python test_integration.py
```

**테스트 항목:**
- ✅ 헬스 체크
- ✅ 사용자 생성/조회/활성화
- ✅ 뉴스 생성/조회/목록
- ✅ 뉴스 상호작용
- ✅ 세션 생성/조회
- ✅ 대화 생성/조회

### 2. 샘플 데이터 생성

테스트용 샘플 데이터를 생성합니다.

```bash
cd system_design
venv311\Scripts\activate
python create_sample_data.py
```

**생성되는 데이터:**
- 👥 사용자 3명 (일반 사용자 2명, 관리자 1명)
- 📰 뉴스 10개 (금융 뉴스)
- 💬 사용자-뉴스 상호작용
- 🔐 세션 및 대화 기록

### 3. Streamlit UI 테스트

#### 백엔드 테스트 페이지

```bash
cd streamlit
..\system_design\venv311\Scripts\activate
streamlit run app.py
```

**기능:**
- 🏥 백엔드 서버 연결 확인
- 👥 사용자 생성/조회/관리
- 📰 뉴스 생성/조회/인기 뉴스
- 💬 세션 및 대화 관리

#### 메인 Streamlit 앱

```bash
cd streamlit
..\system_design\venv311\Scripts\activate
streamlit run app.py
```

**기능:**
- 📰 금융 뉴스 도우미 UI
- 💬 챗봇 패널
- 📊 뉴스 목록 및 상세

---

## 🔍 테스트 시나리오

### 시나리오 1: 기본 연동 테스트

1. **백엔드 서버 실행 확인**
   ```bash
   curl http://localhost:8000/health
   ```
   
2. **Swagger UI에서 API 테스트**
   - http://localhost:8000/docs 접속
   - 각 엔드포인트 테스트

3. **Streamlit 테스트 페이지 실행**
   - http://localhost:8501 접속 (test_backend.py)
   - 헬스 체크 → 사용자 생성 → 뉴스 조회 순서로 테스트

### 시나리오 2: 전체 워크플로우 테스트

1. **샘플 데이터 생성**
   ```bash
   python create_sample_data.py
   ```

2. **통합 테스트 실행**
   ```bash
   python test_integration.py
   ```

3. **Streamlit 앱에서 데이터 확인**
   - 뉴스 목록 조회
   - 인기 뉴스 확인
   - 챗봇과 대화

### 시나리오 3: API 클라이언트 사용

Streamlit 앱 내에서 API 클라이언트 사용:

```python
from api_client import get_api_client

# API 클라이언트 초기화
api = get_api_client("http://localhost:8000")

# 헬스 체크
health = api.health_check()
print(health)

# 뉴스 목록 조회
news_list = api.get_news_list(limit=10)
for news in news_list:
    print(f"[{news['news_id']}] {news['title']}")

# 사용자 생성
user = api.create_user(
    email="test@example.com",
    password="password123",
    username="테스트유저"
)
print(f"User created: {user['user_id']}")
```

---

## 🐛 문제 해결

### 문제 1: 백엔드 서버가 시작되지 않음

**증상:**
```
❌ 서버에 연결할 수 없습니다
```

**해결 방법:**

1. `.env` 파일 확인
   ```bash
   # .env 파일이 있는지 확인
   dir .env
   
   # 없으면 생성
   copy .env.example .env
   ```

2. 데이터베이스 설정 확인
   ```env
   # SQLite 사용 (간단)
   DATABASE_URL=sqlite:///./financefriend.db
   ```

3. 포트 충돌 확인
   ```powershell
   # 포트 8000 사용 확인
   netstat -ano | findstr :8000
   ```

### 문제 2: CORS 에러

**증상:**
```
Access to fetch at 'http://localhost:8000' has been blocked by CORS policy
```

**해결 방법:**

`.env` 파일에서 CORS 설정 확인:
```env
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501
```

### 문제 3: 패키지 설치 오류

**증상:**
```
ModuleNotFoundError: No module named 'fastapi'
```

**해결 방법:**

```bash
# 가상환경 활성화 확인
venv311\Scripts\activate

# 패키지 재설치
pip install -r requirements.txt

# Streamlit용 패키지
cd ..\streamlit
pip install -r requirements.txt
```

### 문제 4: 데이터베이스 연결 오류

**증상:**
```
sqlalchemy.exc.OperationalError: unable to open database file
```

**해결 방법:**

1. SQLite 사용 (간단)
   ```env
   DATABASE_URL=sqlite:///./financefriend.db
   ```

2. PostgreSQL 사용 시
   ```bash
   # PostgreSQL 서비스 시작
   # psql로 데이터베이스 생성
   createdb financefriend
   ```

### 문제 5: Streamlit이 브라우저에서 열리지 않음

**해결 방법:**

수동으로 브라우저에서 접속:
```
http://localhost:8501
```

또는 다른 포트 사용:
```bash
streamlit run test_backend.py --server.port 8502
```

---

## 📊 API 엔드포인트 요약

### 사용자 관리
- `POST /api/v1/users/` - 사용자 생성
- `GET /api/v1/users/` - 사용자 목록
- `GET /api/v1/users/{user_id}` - 사용자 조회
- `POST /api/v1/users/{user_id}/activate` - 사용자 활성화

### 뉴스 관리
- `POST /api/v1/news/` - 뉴스 생성
- `GET /api/v1/news/` - 뉴스 목록
- `GET /api/v1/news/{news_id}` - 뉴스 상세
- `GET /api/v1/news/trending/` - 인기 뉴스
- `POST /api/v1/news/{news_id}/interactions` - 상호작용 생성

### 세션 관리
- `POST /api/v1/sessions/` - 세션 생성
- `GET /api/v1/sessions/{session_id}` - 세션 조회
- `GET /api/v1/sessions/user/{user_id}` - 사용자 세션 목록

### 대화 관리
- `POST /api/v1/dialogues/` - 대화 생성
- `GET /api/v1/dialogues/session/{session_id}` - 세션 대화 목록

---

## 🎯 다음 단계

통합 테스트가 성공적으로 완료되면:

1. **기능 확장**
   - AI 에이전트 통합
   - 뉴스 크롤링 및 임베딩
   - 추천 시스템 구현

2. **배포 준비**
   - Docker 컨테이너화
   - 환경별 설정 분리
   - CI/CD 파이프라인 구성

3. **모니터링**
   - 로깅 시스템 구축
   - 성능 모니터링
   - 에러 추적

---

## 📚 참고 자료

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [SQLAlchemy 공식 문서](https://docs.sqlalchemy.org/)

---

## 💡 도움말

질문이나 문제가 있으면 다음을 확인하세요:

1. **로그 확인**
   - 백엔드: 터미널 출력
   - Streamlit: 브라우저 콘솔 (F12)

2. **API 문서 확인**
   - http://localhost:8000/docs

3. **데이터베이스 확인**
   ```python
   # Python REPL에서
   from database import get_db, init_db
   init_db()
   ```

---

**✨ 테스트를 시작할 준비가 되었습니다!**

```bash
# 간단한 시작 방법
cd system_design
run_servers.bat
```

