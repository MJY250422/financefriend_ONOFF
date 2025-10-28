# 🔗 백엔드-Streamlit 통합 가이드

> 백엔드 API와 Streamlit 웹 애플리케이션의 통합 테스트 환경

## 📁 프로젝트 구조

```
financefriend_ONOFF/
│
├── system_design/                 # 백엔드 서버 (FastAPI)
│   ├── main.py                    # FastAPI 메인 애플리케이션
│   ├── database.py                # 데이터베이스 설정
│   ├── schemas.py                 # Pydantic 스키마
│   ├── enums.py                   # Enum 정의
│   ├── db_schema_design.py        # SQLAlchemy 모델
│   ├── utils.py                   # 유틸리티 함수
│   │
│   ├── routers/                   # API 라우터
│   │   ├── users.py               # 사용자 API
│   │   ├── sessions.py            # 세션 API
│   │   ├── news.py                # 뉴스 API
│   │   ├── dialogues.py           # 대화 API
│   │   └── agent_tasks.py         # 에이전트 작업 API
│   │
│   ├── .env.example               # 환경 설정 예시 ⭐
│   ├── requirements.txt           # Python 패키지
│   │
│   ├── run_servers.bat            # Windows 실행 스크립트 ⭐
│   ├── run_servers.ps1            # PowerShell 실행 스크립트 ⭐
│   ├── test_integration.py        # API 통합 테스트 ⭐
│   ├── create_sample_data.py      # 샘플 데이터 생성 ⭐
│   ├── TEST_GUIDE.md              # 상세 테스트 가이드 ⭐
│   └── QUICK_START.md             # 빠른 시작 가이드 ⭐
│
└── streamlit/                     # Streamlit 웹 앱
    ├── streamlit_app.py.py        # 메인 앱
    ├── api_client.py              # 백엔드 API 클라이언트 ⭐
    ├── test_backend.py            # 백엔드 테스트 페이지 ⭐
    ├── requirements.txt           # Python 패키지 (업데이트됨) ⭐
    │
    ├── core/                      # 핵심 로직
    │   ├── config.py
    │   ├── init_app.py
    │   └── utils.py
    │
    ├── ui/                        # UI 컴포넌트
    │   ├── components/
    │   └── styles.py
    │
    └── data/                      # 데이터 모듈
        └── news.py

⭐ = 새로 추가된 파일
```

## 🚀 빠른 시작

### 1. 환경 설정

```bash
cd system_design
copy .env.example .env
```

### 2. 서버 실행

```bash
# Windows
run_servers.bat

# PowerShell
.\run_servers.ps1
```

### 3. 샘플 데이터 생성

```bash
python create_sample_data.py
```

### 4. 테스트

- **백엔드 API**: http://localhost:8000/docs
- **Streamlit 앱**: http://localhost:8501

## 📚 주요 기능

### 백엔드 API

- ✅ **사용자 관리**: 생성, 조회, 수정, 삭제
- ✅ **뉴스 관리**: 생성, 조회, 검색, 인기 뉴스
- ✅ **상호작용**: 뉴스 클릭, 조회, 좋아요, 공유
- ✅ **세션 관리**: 세션 생성, 조회, 만료 처리
- ✅ **대화 관리**: 사용자-에이전트 대화 기록

### Streamlit 앱

- ✅ **API 클라이언트**: 백엔드 API 호출 라이브러리
- ✅ **테스트 페이지**: 모든 API 테스트 UI
- ✅ **메인 앱**: 금융 뉴스 도우미 UI

## 🛠️ 개발 도구

### API 통합 테스트

```bash
python test_integration.py
```

모든 API 엔드포인트를 자동으로 테스트합니다.

### 샘플 데이터 생성

```bash
python create_sample_data.py
```

- 사용자 3명
- 뉴스 10개
- 상호작용 데이터
- 세션 및 대화 기록

### Streamlit 테스트 페이지

```bash
cd ..\streamlit
streamlit run test_backend.py
```

UI에서 모든 API를 테스트할 수 있습니다.

## 📖 API 문서

### Swagger UI
http://localhost:8000/docs

인터랙티브 API 문서로 직접 API를 테스트할 수 있습니다.

### ReDoc
http://localhost:8000/redoc

보기 좋게 정리된 API 문서입니다.

## 🔧 설정

### 환경 변수 (.env)

```env
# 백엔드 서버
API_HOST=0.0.0.0
API_PORT=8000

# CORS (Streamlit 허용)
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501

# 데이터베이스 (SQLite 또는 PostgreSQL)
DATABASE_URL=sqlite:///./financefriend.db
```

### 데이터베이스

기본적으로 SQLite를 사용하여 별도 설치 없이 바로 시작할 수 있습니다.

PostgreSQL 사용 시:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/financefriend
```

## 🧪 테스트 시나리오

### 시나리오 1: 기본 연동

1. 서버 실행
2. 헬스 체크: `curl http://localhost:8000/health`
3. Swagger UI에서 API 테스트
4. Streamlit 앱에서 UI 확인

### 시나리오 2: 전체 워크플로우

1. 샘플 데이터 생성
2. 통합 테스트 실행
3. Streamlit 앱에서 데이터 확인
4. 대화 기능 테스트

### 시나리오 3: API 클라이언트 사용

```python
from api_client import get_api_client

api = get_api_client()

# 뉴스 목록 조회
news_list = api.get_news_list(limit=10)

# 사용자 생성
user = api.create_user(
    email="test@example.com",
    password="password123",
    username="테스트"
)

# 세션 생성
session = api.create_session(user['user_id'])

# 대화 생성
dialogue = api.create_dialogue(
    session_id=session['session_id'],
    sender_type="USER",
    content="안녕하세요!"
)
```

## 📊 API 엔드포인트

| 카테고리 | 메서드 | 경로 | 설명 |
|---------|--------|------|------|
| 헬스체크 | GET | `/health` | 서버 상태 확인 |
| 사용자 | POST | `/api/v1/users/` | 사용자 생성 |
| 사용자 | GET | `/api/v1/users/` | 사용자 목록 |
| 사용자 | GET | `/api/v1/users/{user_id}` | 사용자 조회 |
| 뉴스 | POST | `/api/v1/news/` | 뉴스 생성 |
| 뉴스 | GET | `/api/v1/news/` | 뉴스 목록 |
| 뉴스 | GET | `/api/v1/news/{news_id}` | 뉴스 상세 |
| 뉴스 | GET | `/api/v1/news/trending/` | 인기 뉴스 |
| 세션 | POST | `/api/v1/sessions/` | 세션 생성 |
| 세션 | GET | `/api/v1/sessions/{session_id}` | 세션 조회 |
| 대화 | POST | `/api/v1/dialogues/` | 대화 생성 |
| 대화 | GET | `/api/v1/dialogues/session/{session_id}` | 세션 대화 목록 |

## 🐛 문제 해결

### 서버가 시작되지 않으면

1. `.env` 파일 확인
2. 가상환경 활성화 확인
3. 패키지 설치: `pip install -r requirements.txt`

### CORS 에러

`.env`에서 `ALLOWED_ORIGINS` 확인:
```env
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501
```

### 포트 충돌

```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

## 📝 더 알아보기

- [TEST_GUIDE.md](TEST_GUIDE.md) - 상세한 테스트 가이드
- [QUICK_START.md](QUICK_START.md) - 빠른 시작 가이드
- [API 문서](http://localhost:8000/docs) - Swagger UI

## 🎯 다음 단계

1. **기능 추가**
   - AI 에이전트 통합
   - 뉴스 크롤러 구현
   - 추천 알고리즘 개발

2. **UI 개선**
   - Streamlit 컴포넌트 커스터마이징
   - 차트 및 시각화 추가
   - 반응형 디자인 적용

3. **배포**
   - Docker 컨테이너화
   - 클라우드 배포 (AWS, GCP, Azure)
   - CI/CD 파이프라인 구축

---

**✨ 즐거운 개발 되세요!**


