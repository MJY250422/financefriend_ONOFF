# FinanceFriend 프로젝트 - 작업 요약 (2025.11.03)

## 📋 작업 개요

오늘 진행한 작업은 **FastAPI 백엔드와 Streamlit 프론트엔드 간의 연결 및 데이터베이스 통합 테스트**입니다.

---

## 🎯 주요 목표

1. FastAPI 백엔드 서버와 Streamlit 프론트엔드 간 연결 확인
2. 데이터베이스 스키마 검증 및 샘플 데이터 생성
3. 전체 시스템 통합 테스트
4. 실제 데이터 수집 준비 완료

---

## 🛠 기술 스택

### Backend (FastAPI)
- **Python 3.11** - 프로그래밍 언어
- **FastAPI** - 고성능 웹 프레임워크
- **SQLAlchemy** - ORM (Object-Relational Mapping)
- **SQLite** - 개발용 데이터베이스
- **Uvicorn** - ASGI 웹 서버
- **Pydantic** - 데이터 검증 및 설정 관리
- **python-dotenv** - 환경 변수 관리

### Frontend (Streamlit)
- **Streamlit** - 데이터 앱 프레임워크
- **Requests** - HTTP 클라이언트 (백엔드 API 호출)

### 데이터베이스
- **SQLite** - 경량 관계형 데이터베이스
  - 개발 단계에서 사용
  - PostgreSQL로 쉽게 전환 가능 (설정만 변경)

### 개발 도구
- **PowerShell** - Windows 터미널
- **venv (Python 3.11)** - 가상 환경

---

## 📁 프로젝트 구조

```
financefriend_ONOFF/
├── system_design/              # 백엔드 (FastAPI)
│   ├── main.py                # FastAPI 메인 애플리케이션
│   ├── database.py            # 데이터베이스 연결 및 세션 관리
│   ├── db_schema_design.py    # SQLAlchemy 모델 정의
│   ├── enums.py               # Enum 타입 정의
│   ├── schemas.py             # Pydantic 스키마
│   ├── utils.py               # 유틸리티 함수 (비밀번호 해싱 등)
│   ├── create_sample_data.py  # 샘플 데이터 생성 스크립트
│   ├── routers/               # API 엔드포인트
│   │   ├── users.py           # 사용자 관련 API
│   │   ├── news.py            # 뉴스 관련 API
│   │   ├── sessions.py        # 세션 관련 API
│   │   ├── dialogues.py       # 대화 관련 API
│   │   └── agent_tasks.py     # 에이전트 작업 관련 API
│   ├── venv311/               # Python 가상 환경
│   └── financefriend.db       # SQLite 데이터베이스 파일
│
├── streamlit/                  # 프론트엔드 (Streamlit)
│   └── app.py                 # Streamlit 메인 애플리케이션
│
└── START.md                   # 프로젝트 시작 가이드
```

---

## 🔧 해결한 주요 문제들

### 1. **UnicodeEncodeError (Emoji 인코딩 문제)**
- **문제**: Windows PowerShell에서 이모지(🚀, ✅ 등) 출력 시 `cp949` 인코딩 오류
- **원인**: Windows 기본 인코딩이 UTF-8이 아님
- **해결**: 모든 print 문의 이모지를 텍스트로 변경 (`[INFO]`, `[OK]`, `[ERROR]` 등)
- **영향 파일**:
  - `main.py`
  - `database.py`
  - `create_sample_data.py`

### 2. **Enum 타입 불일치**
- **문제**: API에서 `"USER"` (대문자) 전송 시 Enum 검증 실패
- **원인**: 
  - `enums.py`: `UserType.USER = "user"` (소문자 value)
  - API 요청: `"USER"` (대문자)
- **해결**:
  - `create_sample_data.py`의 user_type을 소문자로 변경
  - SQLAlchemy Enum에 `native_enum=False` 추가 (SQLite 호환)
- **영향 파일**:
  - `create_sample_data.py`
  - `db_schema_design.py`

### 3. **SQLite Autoincrement 문제**
- **문제**: `NOT NULL constraint failed: news.news_id` 등의 IntegrityError
- **원인**: SQLite에서 `BigInteger`와 `autoincrement=True` 조합이 제대로 작동하지 않음
- **해결**: 모든 auto-increment 컬럼을 `Integer PRIMARY KEY`로 변경
  - SQLite는 `INTEGER PRIMARY KEY`만 있으면 자동으로 ROWID를 사용하여 auto-increment 처리
- **변경 사항**:
  ```python
  # Before
  news_id = Column(BigInteger, primary_key=True, autoincrement=True)
  
  # After
  news_id = Column(Integer, primary_key=True)
  ```
- **영향 컬럼**: `news_id`, `embedding_id`, `interaction_id`, `task_id`, `dialogue_id`

### 4. **PowerShell 실행 정책 문제**
- **문제**: 가상 환경 활성화 시 `PSSecurityException` 발생
- **해결**: PowerShell 실행 정책 변경
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### 5. **Python 모듈 캐시 문제**
- **문제**: 코드 수정 후에도 변경사항이 반영되지 않음
- **해결**: `__pycache__` 디렉토리와 `.pyc` 파일 삭제
  ```powershell
  Get-ChildItem -Recurse -Include "__pycache__" -Directory | Remove-Item -Recurse -Force
  ```

---

## ✅ 생성된 샘플 데이터

### 사용자 (Users) - 3명
- `user1@example.com` - 김철수 (일반 사용자)
- `user2@example.com` - 이영희 (일반 사용자)
- `admin@example.com` - 관리자 (관리자)

### 뉴스 (News) - 10개
1. 한국은행, 기준금리 3.5% 동결
2. 삼성전자, 3분기 배당 30% 증액 발표
3. 원/달러 환율 1,300원 돌파
4. 코스피, 연중 최저치 2,500선 회복
5. 미국, 인플레 압력 완화 신호
6. 현대차, 전기차 판매 급증
7. SK하이닉스, AI 반도체 투자 확대
8. 카카오, 자회사 구조 개편 발표
9. KB금융, 디지털 전환 로드맵 발표
10. 네이버, 클라우드 사업 본격화

### 상호작용 (Interactions) - 11개
- 사용자들의 뉴스 조회, 클릭, 공유, 좋아요 기록

### 세션 (Sessions) - 3개
- 각 사용자별 활성 세션

### 대화 (Dialogues) - 6개
- 사용자-AI 어시스턴트 간 대화 샘플

---

## 🚀 실행 방법

### 1. 백엔드 서버 시작

```powershell
cd system_design
python main.py
```

**확인사항**:
- 서버가 `http://localhost:8000`에서 실행됨
- `Application startup complete` 메시지 확인
- API 문서: `http://localhost:8000/docs`

### 2. Streamlit 앱 시작

```powershell
cd ..
streamlit run streamlit/app.py
```

**확인사항**:
- 앱이 `http://localhost:8501`에서 실행됨
- 브라우저가 자동으로 열림
- 생성된 샘플 데이터 확인 가능

### 3. 샘플 데이터 재생성 (필요시)

```powershell
cd system_design
python create_sample_data.py
```

---

## 🔌 API 엔드포인트

### Users
- `POST /api/v1/users/` - 사용자 생성
- `GET /api/v1/users/` - 사용자 목록 조회
- `GET /api/v1/users/{user_id}` - 특정 사용자 조회
- `PUT /api/v1/users/{user_id}` - 사용자 정보 수정
- `DELETE /api/v1/users/{user_id}` - 사용자 삭제 (Soft Delete)

### News
- `POST /api/v1/news/` - 뉴스 생성
- `GET /api/v1/news/` - 뉴스 목록 조회
- `GET /api/v1/news/{news_id}` - 특정 뉴스 조회
- `PUT /api/v1/news/{news_id}` - 뉴스 수정
- `DELETE /api/v1/news/{news_id}` - 뉴스 삭제

### Sessions
- `POST /api/v1/sessions/` - 세션 생성
- `GET /api/v1/sessions/` - 세션 목록 조회
- `GET /api/v1/sessions/{session_id}` - 특정 세션 조회

### Dialogues
- `POST /api/v1/dialogues/` - 대화 생성
- `GET /api/v1/dialogues/` - 대화 목록 조회
- `GET /api/v1/dialogues/session/{session_id}/history` - 세션 대화 이력

### Agent Tasks
- `POST /api/v1/agent-tasks/` - 작업 생성
- `GET /api/v1/agent-tasks/` - 작업 목록 조회

---

## 📊 데이터베이스 스키마

### 주요 테이블

1. **users** - 사용자 정보
   - user_id (PK, UUID)
   - email, username, password_hash
   - user_type (admin, user, guest, premium)

2. **news** - 뉴스 데이터
   - news_id (PK, auto-increment)
   - title, url, content, source
   - published_at, created_at

3. **sessions** - 세션 관리
   - session_id (PK, auto-increment)
   - user_id (FK)
   - session_token, created_at, expires_at

4. **dialogues** - 대화 기록
   - dialogue_id (PK, auto-increment)
   - session_id (FK)
   - sender_type (user, assistant, system)
   - content, intent

5. **user_news_interactions** - 사용자-뉴스 상호작용
   - interaction_id (PK, auto-increment)
   - user_id (FK), news_id (FK)
   - interaction_type (click, view, share, like, bookmark)

6. **news_embeddings** - 뉴스 벡터 임베딩
   - embedding_id (PK, auto-increment)
   - news_id (FK)
   - embedding_vector, model_version

7. **agent_tasks** - AI 에이전트 작업
   - task_id (PK, auto-increment)
   - agent_id (FK), session_id (FK)
   - input_data, output_data, status

8. **agent_info** - 에이전트 메타데이터
   - agent_id (PK, auto-increment)
   - agent_name, agent_type, config

---

## 🎓 학습 포인트

### 1. FastAPI + SQLAlchemy 패턴
- Dependency Injection을 통한 DB 세션 관리
- Pydantic을 통한 자동 데이터 검증
- 비동기 처리 지원

### 2. SQLite 특성
- `INTEGER PRIMARY KEY`는 자동으로 ROWID를 사용
- `BigInteger`는 autoincrement와 함께 사용 시 문제 발생 가능
- Enum 타입은 `native_enum=False` 옵션 필요

### 3. Windows 환경 개발
- 인코딩 문제 (cp949 vs UTF-8)
- PowerShell 실행 정책
- 가상 환경 활성화 방법

### 4. 디버깅 전략
- 단계별 접근 (Users → News → Sessions → Dialogues)
- 백엔드 로그 확인의 중요성
- 데이터베이스 파일 및 캐시 정리

---

## 🔜 다음 단계

1. **실제 뉴스 데이터 수집**
   - 뉴스 API 연동 또는 크롤링
   - 정기적인 데이터 업데이트 스케줄링

2. **AI 에이전트 구현**
   - LangChain 또는 OpenAI API 연동
   - 뉴스 요약 및 추천 로직

3. **프론트엔드 개선**
   - 사용자 인터페이스 개선
   - 실시간 뉴스 피드
   - 개인화된 추천 시스템

4. **프로덕션 준비**
   - PostgreSQL로 DB 전환
   - 배포 환경 설정 (Docker, AWS 등)
   - 인증/인가 시스템 강화

---

## 📝 참고사항

### 환경 변수 설정 (.env)
```env
DATABASE_URL=sqlite:///./financefriend.db
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
ALLOWED_ORIGINS=http://localhost:8501
```

### 가상 환경 활성화
```powershell
# PowerShell
.\venv311\Scripts\Activate.ps1

# CMD
.\venv311\Scripts\activate.bat
```

### 데이터베이스 초기화 (필요시)
```powershell
# 데이터베이스 파일 삭제
Remove-Item financefriend.db

# 백엔드 재시작하면 자동으로 테이블 생성됨
python main.py
```

---

## 👥 팀원 가이드

### 처음 시작하는 경우
1. Python 3.11 설치 확인
2. 가상 환경 생성 및 활성화
3. 의존성 패키지 설치: `pip install -r requirements.txt`
4. 백엔드 서버 시작
5. Streamlit 앱 시작
6. 샘플 데이터 생성

### 개발 시 주의사항
- 백엔드 코드 수정 후 서버 재시작 필요 (또는 `reload=True` 설정)
- 스키마 변경 시 데이터베이스 초기화 필요
- Windows에서 이모지 사용 금지 (인코딩 문제)

---

## 📞 문제 발생 시

### 백엔드가 시작되지 않을 때
1. 포트 8000이 사용 중인지 확인
2. Python 캐시 삭제: `Remove-Item -Recurse __pycache__`
3. 가상 환경이 활성화되어 있는지 확인

### Streamlit이 백엔드에 연결되지 않을 때
1. 백엔드가 실행 중인지 확인 (`http://localhost:8000/health`)
2. CORS 설정 확인 (`ALLOWED_ORIGINS` 환경 변수)
3. 네트워크 방화벽 확인

### 데이터베이스 에러
1. DB 파일 삭제 후 재생성
2. 스키마 변경사항 확인
3. SQLAlchemy 로그 확인 (`echo=True` 설정)

---

**작성일**: 2025년 11월 3일  
**작성자**: AI Assistant  
**프로젝트**: FinanceFriend News Agent


