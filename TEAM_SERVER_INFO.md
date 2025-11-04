# 팀원용 서버 접속 정보

> **FinanceFriend 백엔드 API 서버 접속 가이드**

---

## 🖥️ 서버 정보

### 기본 설정
- **포트 번호**: `8000`
- **프로토콜**: `HTTP`
- **호스트**: `0.0.0.0` (모든 네트워크 인터페이스)

---

## 🌐 접속 방법

### 방법 1: 로컬 접속 (서버와 같은 컴퓨터)

```
Base URL: http://localhost:8000
```

**주요 엔드포인트**:
- 📚 **API 문서 (Swagger)**: http://localhost:8000/docs
- 📖 **API 문서 (ReDoc)**: http://localhost:8000/redoc
- ❤️ **Health Check**: http://localhost:8000/health
- 📰 **뉴스 목록**: http://localhost:8000/api/v1/news/
- 👤 **사용자 목록**: http://localhost:8000/api/v1/users/

---

### 방법 2: 네트워크 접속 (다른 컴퓨터)

#### Step 1: 서버 관리자의 IP 주소 확인

서버를 실행하는 사람이 확인:
```powershell
ipconfig
```

**찾을 내용**: IPv4 주소 (예: `192.168.0.10`)

#### Step 2: 팀원 접속

```
Base URL: http://[서버_IP]:8000
```

**예시** (서버 IP가 192.168.0.10인 경우):
```
Base URL: http://192.168.0.10:8000
Swagger UI: http://192.168.0.10:8000/docs
Health Check: http://192.168.0.10:8000/health
```

---

## 🔧 현재 서버 설정

```env
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
```

---

## 📡 API 엔드포인트 목록

### Health Check
```
GET http://localhost:8000/health
GET http://localhost:8000/
```

**응답 예시**:
```json
{
  "status": "healthy",
  "message": "All systems operational",
  "version": "1.0.0"
}
```

### 사용자 (Users)
```
GET    /api/v1/users/              - 사용자 목록
POST   /api/v1/users/              - 사용자 생성
GET    /api/v1/users/{user_id}     - 특정 사용자 조회
PUT    /api/v1/users/{user_id}     - 사용자 수정
DELETE /api/v1/users/{user_id}     - 사용자 삭제
```

### 뉴스 (News)
```
GET    /api/v1/news/               - 뉴스 목록
POST   /api/v1/news/               - 뉴스 생성
GET    /api/v1/news/{news_id}      - 특정 뉴스 조회
PUT    /api/v1/news/{news_id}      - 뉴스 수정
DELETE /api/v1/news/{news_id}      - 뉴스 삭제
POST   /api/v1/news/{news_id}/interactions - 상호작용 기록
```

### 세션 (Sessions)
```
GET    /api/v1/sessions/           - 세션 목록
POST   /api/v1/sessions/           - 세션 생성
GET    /api/v1/sessions/{id}       - 세션 조회
PUT    /api/v1/sessions/{id}/context - 세션 컨텍스트 업데이트
```

### 대화 (Dialogues)
```
GET    /api/v1/dialogues/          - 대화 목록
POST   /api/v1/dialogues/          - 대화 생성
GET    /api/v1/dialogues/session/{session_id}/history - 대화 이력
```

### 에이전트 작업 (Agent Tasks)
```
GET    /api/v1/agent-tasks/        - 작업 목록
POST   /api/v1/agent-tasks/        - 작업 생성
PUT    /api/v1/agent-tasks/{id}    - 작업 업데이트
```

**전체 API 문서**: http://localhost:8000/docs

---

## 🧪 연결 테스트 방법

### 브라우저에서 테스트
```
http://localhost:8000/health
```

**성공 시**: JSON 응답 표시
```json
{"status": "healthy", "message": "All systems operational", "version": "1.0.0"}
```

### PowerShell에서 테스트
```powershell
# Health Check
Invoke-WebRequest -Uri "http://localhost:8000/health" | Select-Object -ExpandProperty Content

# 뉴스 목록 조회
Invoke-WebRequest -Uri "http://localhost:8000/api/v1/news/" | Select-Object -ExpandProperty Content
```

### Python에서 테스트
```python
import requests

# Health Check
response = requests.get("http://localhost:8000/health")
print(response.json())

# 뉴스 목록
response = requests.get("http://localhost:8000/api/v1/news/")
print(response.json())
```

---

## ⚠️ 네트워크 접속 시 주의사항

### 1. 방화벽 설정 필요

서버 관리자가 실행:
```powershell
# 8000번 포트 허용
netsh advfirewall firewall add rule name="FastAPI Server" dir=in action=allow protocol=TCP localport=8000
```

### 2. 같은 네트워크 필수
- 같은 WiFi 또는 LAN에 연결되어 있어야 함
- 외부 인터넷에서는 접속 불가 (포트 포워딩 없이)

### 3. CORS 설정 확인

`.env` 파일에 팀원 IP 추가 필요할 수 있음:
```env
ALLOWED_ORIGINS=http://localhost:8501,http://192.168.0.10:8501,http://팀원IP:8501
```

---

## 🔄 서버 시작 방법

### 서버 관리자가 실행:

```powershell
# 1. 프로젝트 디렉토리로 이동
cd system_design

# 2. 가상 환경 활성화
.\venv311\Scripts\Activate.ps1

# 3. 서버 시작
python main.py
```

**확인**:
```
[INFO] Starting News Agent API...
[SUCCESS] Database initialized
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

---

## 🌍 Streamlit 앱 주소 (프론트엔드)

### 로컬
```
http://localhost:8501
```

### 네트워크
```
http://[서버_IP]:8501
```

---

## 📊 서버 상태 확인

### 실행 중인지 확인
```powershell
# 8000번 포트 사용 중인지 확인
netstat -ano | findstr :8000
```

### 프로세스 확인
```powershell
Get-Process python
```

---

## 🐛 문제 해결

### 문제 1: "연결할 수 없음" (Connection Refused)
```
원인: 서버가 실행되지 않음
해결: 서버 관리자에게 서버 시작 요청
```

### 문제 2: "타임아웃" (Timeout)
```
원인: 방화벽 차단 또는 다른 네트워크
해결: 
1. 방화벽 규칙 추가
2. 같은 WiFi/LAN 연결 확인
3. IP 주소 재확인
```

### 문제 3: "404 Not Found"
```
원인: 잘못된 엔드포인트 경로
해결: Swagger UI에서 올바른 경로 확인
http://localhost:8000/docs
```

### 문제 4: "CORS 에러"
```
원인: CORS 설정에 허용되지 않은 Origin
해결: 서버 관리자가 .env 파일의 ALLOWED_ORIGINS에 추가
```

---

## 📞 서버 관리자 연락처

서버 문제 발생 시:
1. 팀 채팅방에 문의
2. 서버 관리자에게 DM
3. 이 문서의 문제 해결 섹션 참고

---

## 🚀 빠른 참조

```
Base URL (로컬):     http://localhost:8000
Base URL (네트워크): http://[서버IP]:8000
API 문서:           /docs
Health Check:       /health
뉴스 API:          /api/v1/news/
사용자 API:        /api/v1/users/
세션 API:          /api/v1/sessions/
대화 API:          /api/v1/dialogues/
```

---

## 📚 추가 문서

- **API_CONNECTION_GUIDE.md**: 상세 API 사용법
- **SUPABASE_SETUP.md**: 데이터베이스 설정
- **TEAM_SETUP_GUIDE.md**: 개발 환경 설정

---

**마지막 업데이트**: 2025.11.04  
**서버 버전**: 1.0.0  
**포트**: 8000

**문의사항은 팀 채팅방으로!** 💬

