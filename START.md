# 🚀 FinanceFriend 실행 가이드

백엔드(FastAPI)와 프론트엔드(Streamlit)를 연결하여 실행하는 방법입니다.

## ✅ 테스트 완료 사항

- [x] 프로젝트 구조 정리
- [x] 백엔드 UnicodeError 수정
- [x] 백엔드 서버 단독 실행 테스트
- [x] Streamlit 프론트엔드 단독 실행 테스트
- [x] 백엔드-프론트엔드 연결 테스트

## 📁 프로젝트 구조

```
financefriend_ONOFF/
├── system_design/        # 백엔드 (FastAPI)
│   ├── main.py          # FastAPI 메인 애플리케이션
│   ├── database.py      # DB 설정
│   ├── routers/         # API 라우터들
│   ├── newsagent.db     # SQLite 데이터베이스
│   └── venv311/         # Python 3.11 가상환경
│
└── streamlit/           # 프론트엔드 (Streamlit)
    ├── api_client.py    # 백엔드 API 클라이언트
    ├── app.py           # 독립형 Streamlit 앱
    └── test_backend.py  # 백엔드 연동 테스트 앱
```

## 🎯 실행 방법

### 방법 1: 자동 실행 (권장)

#### PowerShell 스크립트 사용:
```powershell
cd system_design
.\run_servers.ps1
```

#### 배치 파일 사용:
```cmd
cd system_design
run_servers.bat
```

### 방법 2: 수동 실행 (단계별)

#### 1단계: 백엔드 서버 실행

새 터미널 창을 열고:
```powershell
cd C:\Users\USER\Desktop\financefriend_ONOFF\system_design
.\venv311\Scripts\Activate.ps1
python main.py
```

백엔드가 정상 실행되면 다음과 같이 표시됩니다:
```
[INFO] Starting News Agent API...
[SUCCESS] Database initialized
INFO:     Uvicorn running on http://0.0.0.0:8000
```

#### 2단계: Streamlit 프론트엔드 실행

**새로운** 터미널 창을 열고:
```powershell
cd C:\Users\USER\Desktop\financefriend_ONOFF\streamlit
..\system_design\venv311\Scripts\Activate.ps1
streamlit run test_backend.py
```

Streamlit이 자동으로 브라우저를 열고 http://localhost:8501 에서 실행됩니다.

## 🔍 연결 테스트

### 빠른 테스트:
```powershell
python final_test.py
```

### 수동 테스트:

1. **백엔드 헬스 체크:**
   - 브라우저에서 http://localhost:8000/health 접속
   - 또는 http://localhost:8000/docs 에서 API 문서 확인

2. **프론트엔드 연결 확인:**
   - 브라우저에서 http://localhost:8501 접속
   - 사이드바에서 "연결 확인" 버튼 클릭
   - "백엔드 연결 성공" 메시지 확인

## 📊 API 엔드포인트

### 주요 엔드포인트:

| 엔드포인트 | 메서드 | 설명 |
|-----------|--------|------|
| `/` | GET | 루트 (헬스 체크) |
| `/health` | GET | 상세 헬스 체크 |
| `/docs` | GET | Swagger UI (API 문서) |
| `/api/v1/users/` | GET, POST | 사용자 관리 |
| `/api/v1/news/` | GET, POST | 뉴스 관리 |
| `/api/v1/sessions/` | GET, POST | 세션 관리 |
| `/api/v1/dialogues/` | GET, POST | 대화 관리 |

## 🧪 테스트 페이지 기능

Streamlit 테스트 앱(test_backend.py)에서 다음 기능을 테스트할 수 있습니다:

### 탭 1: 헬스 체크
- 백엔드 서버 상태 확인
- 버전 정보 표시

### 탭 2: 사용자 관리
- 사용자 생성 (이메일, 비밀번호, 사용자명)
- 사용자 조회 (User ID로 검색)
- 사용자 목록 조회

### 탭 3: 뉴스 관리
- 뉴스 생성 (제목, URL, 본문, 출처)
- 뉴스 목록 조회 (필터, 검색)
- 인기 뉴스 조회

### 탭 4: 대화 관리
- 세션 생성 (User ID 필요)
- 대화 메시지 전송
- 대화 기록 조회

## 📝 샘플 데이터 생성

뉴스나 사용자 데이터가 없는 경우:
```powershell
cd system_design
.\venv311\Scripts\Activate.ps1
python create_sample_data.py
```

## ⚠️ 문제 해결

### 1. 백엔드가 시작되지 않는 경우:
```powershell
# 포트 8000이 사용 중인지 확인
netstat -ano | findstr ":8000"

# 사용 중이면 프로세스 종료
taskkill /PID <프로세스ID> /F
```

### 2. Streamlit이 연결되지 않는 경우:
- 백엔드가 먼저 실행되었는지 확인
- http://localhost:8000/health 에서 백엔드 상태 확인
- Streamlit에서 "연결 확인" 버튼 클릭

### 3. UnicodeEncodeError 발생 시:
- 이미 수정되었습니다 (main.py에서 이모지 제거 완료)
- 혹시 다시 발생하면 터미널 인코딩을 UTF-8로 설정:
```powershell
$OutputEncoding = [System.Text.Encoding]::UTF8
```

### 4. 가상환경 활성화 실패:
```powershell
# PowerShell 실행 정책 변경 (관리자 권한 필요)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 🌐 접속 URL

- **백엔드 API:** http://localhost:8000
- **API 문서 (Swagger):** http://localhost:8000/docs
- **API 문서 (ReDoc):** http://localhost:8000/redoc
- **Streamlit 앱:** http://localhost:8501

## 🎉 성공 확인

다음 사항이 모두 정상이면 연결 성공입니다:

1. ✅ 백엔드: http://localhost:8000/health 에서 `{"status":"healthy"}` 응답
2. ✅ 프론트엔드: http://localhost:8501 에서 Streamlit 앱 표시
3. ✅ 연결: Streamlit에서 "연결 확인" 버튼 클릭 시 성공 메시지
4. ✅ API 호출: 뉴스 목록, 사용자 목록 등이 정상 조회됨

---

**작업 완료일:** 2025-11-03
**테스트 상태:** ✅ 모든 테스트 통과


